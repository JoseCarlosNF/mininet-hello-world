from mininet.topo import Topo


class HelloTopology(Topo):
    def build(self):
        h1 = self.addHost('h1')
        s1 = self.addSwitch('s1')
        self.addLink(h1, s1)


topos = {'HelloTopology': (lambda: HelloTopology())}
