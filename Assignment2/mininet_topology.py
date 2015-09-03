
#!/usr/bin/python

from mininet.topolib import TreeTopo
from mininet.net import Mininet
from mininet.node import Controller,RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
import sys

def createNet(args):
    
    X=int(args[1])
    Y=int(args[2])
    hosts=[]
    switches=[]
        
    "Create an empty network and add nodes to it."
    net=Mininet(controller=Controller,link=TCLink)
    #net = Mininet(autoStaticArp=True,link=TCLink)

    info( '*** Adding controller\n' )
    net.addController('c0')
    #net.addController(controller=RemoteController)

    info( '*** Adding hosts\n' )
    totalhosts=X*Y
    limit=totalhosts+1
    for i in range(1,limit):
        if(i%2==0):
            ip='10.0.0.'+str(i)
            hostname='h'+str(i)
            hosts.append(net.addHost(hostname,ip=ip))
        else:
            ip='11.0.0.'+str(i)
            hostname='h'+str(i)
            hosts.append(net.addHost(hostname,ip=ip))
    
    info( '*** Adding switch\n' )
    limit=Y+1
    for i in range(1,limit):
        switchname='s'+str(i)
        switches.append(net.addSwitch(switchname))

    info( '*** Creating links\n' )
    index=0
    for s in switches:
        for i in range(X):
            obj=net.addLink(hosts[index],s)
            if((index+1)%2==0):
                obj.intf1.config(bw=2)
            else:
                obj.intf1.config(bw=1)              
            index=index+1

    for i in range(Y-1):
        net.addLink(switches[i],switches[i+1])

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    args=sys.argv
    if(len(args)<3):
        print "pass two arguments:No of hosts per switch and No of switches"
    else:
        createNet(args)
