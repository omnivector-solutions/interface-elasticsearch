from charms.reactive import set_flag, clear_flag
from charms.reactive import Endpoint


class ElasticsearchProvides(Endpoint):
    def configure(self, host, port, cluster_name):
        """
        Configure the host-port relation by providing a port and host.

        """
        for relation in self.relations:
            relation.send['cluster_name'] = cluster_name
            relation.send['host'] = host
            relation.send['port'] = port
