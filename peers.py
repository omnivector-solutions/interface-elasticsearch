from charms.reactive import set_flag, clear_flag, when
from charms.reactive import Endpoint


class ElasticsearchPeer(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def peer_joined(self):
        set_flag(self.flag('endpoint.{endpoint_name}.cluster.joined'))
        clear_flag(self.flag('endpoint.{endpoint_name}.joined'))

    @when('endpoint.{endpoint_name}.departed')
    def peer_departed(self):
        set_flag(self.flag('endpoint.{endpoint_name}.cluster.departed'))
        clear_flag(self.flag('endpoint.{endpoint_name}.departed'))

    def peer_info(self):
        """
        Helper to give all members access to the other peer's
        unit info.

        """
        return self.all_units
