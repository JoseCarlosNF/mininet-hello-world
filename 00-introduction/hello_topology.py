from mininet.topo import Topo


class HelloTopology(Topo):
    def build(self):
        # Hosts
        n_hosts = 5
        hosts = []
        for n in range(1, n_hosts + 1):
            hosts.append(self.addHost('h' + str(n)))

        # Switches
        n_switches = 1
        switches = []
        for n in range(1, n_switches + 1):
            switches.append(self.addSwitch('s' + str(n)))

        # Likns to all hosts to s1
        for host in hosts:
            self.addLink(host, switches[0])


topos = {'HelloTopology': (lambda: HelloTopology())}
