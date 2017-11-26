# Overview

This interface layer is based off the `http` interface 
(most of the code here was initially shamelessly stolen from [here](https://github.com/juju-solutions/interface-http).


# Usage

## Provides

```python
from charmhelpers.core.hookenv import status_set, network_get
from charms.reactive import set_flag, clear_flag
from charms.reactive import when
from charms.reactive import context


@when('endpoint.http.joined')
def configure_website():
    my_ingress_address = network_get("http")['ingress-addresses'][0]
    context.endpoints.http.configure(80, my_ingress_address)
    status_set('active', "HTTP interface configured")


@when('endpoint.member.cluster.joined')
def write_peers_out():
    peers = context.endpoints.member.peer_info()
    peers_addresses = []
    if len(peers) > 0:
        for peer in peers:
            peers_addresses.append(peer._data['private-address'])
        with open('/home/ubuntu/mypeers.txt', 'w') as f:
            f.write(",".join(peers_addresses))

    clear_flag('endpoint.member.cluster.joined')
```

## Requires

```python
from charmhelpers.core import hookenv
from charms.reactive import when
from charms.reactive import clear_flag
from charms.reactive import context


@when('endpoint.http.host-port')
def update_reverse_proxy_config():
    hosts = []
    for my_unit in context.endpoints.http.relation_data():
        hookenv.log('New website: {}:{}'.format(
            my_unit['host'],
            my_unit['port']))
        hosts.append(my_unit['host'])

    hookenv.status_set('active', ",".join(hosts))

    clear_flag('endpoint.http.host-port')
```
