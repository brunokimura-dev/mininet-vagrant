#!/usr/bin/python

import time
import sys
import argparse
import math

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.clean import cleanup
from datetime import datetime


class NetTopo(Topo):
        def build(self, **_opts):
                c = self.addHost('c')
                s = self.addHost('s')
                r1 = self.addHost('r1')
                r2 = self.addHost('r2')
                self.addLink(r1, r2, intfName1='r1-eth0', intfName2='r2-eth0')
                self.addLink(c, r1, intfName1='c-eth0', intfName2='r1-eth1')
                self.addLink(s, r2, intfName1='s-eth0', intfName2='r2-eth1')


def create_ip_net(net):
        print "create_ip_net"
        net['c' ].cmdPrint("ifconfig c-eth0 192.168.1.2/24")
        net['r1'].cmdPrint("ifconfig r1-eth1 192.168.1.1/24")
        net['r1'].cmdPrint("ifconfig r1-eth0 10.0.0.1/30")
        net['s' ].cmdPrint("ifconfig s-eth0 192.168.2.2/24")
        net['r2'].cmdPrint("ifconfig r2-eth1 192.168.2.1/24")
        net['r2'].cmdPrint("ifconfig r2-eth0 10.0.0.2/30")

def config_route(net):
        print "config_route"
        net['c' ].cmdPrint('route add default gw 192.168.1.1')
        net['s' ].cmdPrint('route add default gw 192.168.2.1')
        net['r1'].cmdPrint('sysctl -w net.ipv4.ip_forward=1')
        net['r2'].cmdPrint('sysctl -w net.ipv4.ip_forward=1')
        net['r1'].cmdPrint('route add -net 192.168.2.0/30 gw 10.0.0.2 dev r1-eth0')
        net['r2'].cmdPrint('route add -net 192.168.1.0/30 gw 10.0.0.1 dev r2-eth0')

def net_test(net):
        print "Network connectivity"
        net['c'].cmdPrint('ping -c 3 192.168.2.2')
        net['c'].cmdPrint('traceroute 192.168.2.2')
        net['s'].cmdPrint('iperf3 -s &')
        net['c'].cmdPrint('sleep 3')
        net['c'].cmdPrint('iperf3 -c 192.168.2.2 -R -t 10 -P 1')

def run():
        topo = NetTopo()
        net = Mininet(topo=topo) #, link=TCLink, switch=OVSBridge, controller=None, host=CPULimitedHost)
        net.start()
        print "Host connections"
        dumpNodeConnections(net.hosts)

        create_ip_net(net)
        config_route(net)

        net_test(net)

        CLI(net)
        net.stop()
        cleanup()

if __name__ == '__main__':
        setLogLevel( 'info' )
        run()
