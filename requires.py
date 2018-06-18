from charms.reactive import when, when_not, when_any
from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint


class ElasticsearchRequires(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        if any(unit.received['port'] for unit in self.all_units):
            set_flag(self.expand_name('endpoint.{endpoint_name}.available'))

    @when_any('endpoint.{endpoint_name}.changed.host',
              'endpoint.{endpoint_name}.changed.port',
              'endpoint.{endpoint_name}.changed.cluster_name')
    def changed(self):
        if any(unit.received['port'] for unit in self.all_units):
            set_flag(self.expand_name('endpoint.{endpoint_name}.available'))

    @when_not('endpoint.{endpoint_name}.joined')
    def broken(self):
        clear_flag(self.expand_name('endpoint.{endpoint_name}.available'))
        

    def list_unit_data(self):
        """
        Get the list of the relation info for each unit.

        Returns a list of dicts, where each dict contains the elasticsearch
        cluster name, the host (address)
        and the port (as a string), as well as
        the relation ID and remote unit name that provided the site.

        For example::
            [
                {
                    'host': '10.1.1.1',
                    'port': '80',
                    'cluster_name': "elasticsearch"
                    'relation_id': 'reverseproxy:1',
                    'unit_name': 'myblog/0',
                },
            ]
        """
        units_data = []
        for relation in self.relations:
            for unit in relation.units:
                host = unit.received['host']
                port = unit.received['port']
                cluster_name = unit.received['cluster_name']
                if not (host and port and cluster_name):
                    continue
                units_data.append({
                    'host': host,
                    'port': port,
                    'cluster_name': cluster_name,
                    'relation_id': relation.relation_id,
                    'unit_name': unit.unit_name,
                })
        return units_data
