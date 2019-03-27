from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
import socket

#!/usr/bin/env python
import socket
TCP_IP = '138.68.8.245'
TCP_PORT = 8500
MESSAGE = "Hello, World!"


class Echo(DatagramProtocol):
        

    def datagramReceived(self, data, (host, port)):
        print "received %r from %s:%d" % (data, host, port)
        self.transport.write(data, (host, port))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(data)
        s.close()

reactor.listenUDP(8500, Echo())
reactor.run()
