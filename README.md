# Interface Elasticsearch

Interface for communicating with Elasticsearch.


### Usage
Client charms connecting to elasticsearch via the [requires](requires.py) side of this 
interface can gate against the `'endpoint.elasticsearch.available'` flag set by 
the [provides](provides.py) side of the interface.

#### Example Charm Code

```python
@reactive.when('endpoint.elasticsearch.available')
def render_elasticsearch_lb():
    """Get Elasticsearch cluster nodes.
    """
    hookenv.status_set('maintenance',
                       'Configuring application for elasticsearch')

    ES_SERVERS = []
    for es in reactive.endpoint_from_flag(
       'endpoint.elasticsearch.available').list_unit_data():
            ES_SERVERS.append("{}:{}".format(es['host'], es['port']))

    kv.set('es_hosts', ES_SERVERS)
```

### Contact
* Omnivector Solutions <info@omnivector.solutions>
