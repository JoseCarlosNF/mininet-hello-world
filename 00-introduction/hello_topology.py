from mininet.link import TCLink
from mininet.topo import Topo


class HelloTopology(Topo):
    def build(self):
        # Hosts
        n_hosts = 10
        hosts = []
        for n in range(1, n_hosts + 1):
            hosts.append(self.addHost('h' + str(n)))

        # Switches
        n_switches = 2
        switches = []
        for n in range(1, n_switches + 1):
            switches.append(self.addSwitch('s' + str(n)))

        # Likns to hosts 1-5 to s1
        for host in hosts[:5]:
            self.addLink(host, switches[0], cls=TCLink, bw=100)

        # Likns to hosts 6-10 to s2
        for host in hosts[5:]:
            self.addLink(host, switches[1])

        self.addLink(
            hosts[0], switches[0], cls=TCLink, bw=10, delay='500ms', loss=80
        )


topos = {'HelloTopology': (lambda: HelloTopology())}
