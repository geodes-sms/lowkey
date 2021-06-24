#!/usr/bin/env python
import zmq

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Server
"""


# simple struct for routing information for a key-value snapshot
class Route:

    def __init__(self, socket, identity):
        self.socket = socket  # ROUTER socket to send to
        self.identity = identity  # Identity of peer who requested state


class Server():

    def send_single(self, key, kvmsg, route):
        """Send one state snapshot key-value pair to a socket"""
        # Send identity of recipient first
        route.socket.send(route.identity, zmq.SNDMORE)  # @UndefinedVariable
        kvmsg.send(route.socket)
    
    def __init__(self):
        ctx = zmq.Context()
        
        self._snapshot = ctx.socket(zmq.ROUTER)  # @UndefinedVariable
        self._snapshot.bind("tcp://*:5556")
        self._publisher = ctx.socket(zmq.PUB)  # @UndefinedVariable
        self._publisher.bind("tcp://*:5557")
        self._collector = ctx.socket(zmq.PULL)  # @UndefinedVariable
        self._collector.bind("tcp://*:5558")
        
        self._poller = zmq.Poller()
        self._poller.register(self._collector, zmq.POLLIN)  # @UndefinedVariable
        self._poller.register(self._snapshot, zmq.POLLIN)  # @UndefinedVariable
    
    def run(self):
        sequence = 0
        msg = ""
        
        while True:
            try:
                items = dict(self._poller.poll(1000))
            except:
                break
            
            # PULLed messages PUBLISHED by the clients
            if self._collector in items:
                msg = self._collector.recv_multipart()
                identity = msg[0]
                request = msg[1]
                print(request)
                sequence += 1
                print("I: publishing update %5d" % sequence)
                self._publisher.send(b'This was published by the srv.')
            
            # snapshot requests by joining clients
            if self._snapshot in items:
                msg = self._snapshot.recv_multipart()
                identity = msg[0]
                request = msg[1]
                print("Identity: {}".format(identity))
                print("Request: {}".format(request))
                if request == b"ICANHAZ?":
                    pass
                else:
                    print("E: bad request, aborting\n")
                    break
    
                route = Route(self._snapshot, identity)
    
                route.socket.send(route.identity, zmq.SNDMORE)  # @UndefinedVariable
                self._snapshot.send(b'asd')
    
                print("Sending state shapshot=%d\n" % sequence)
                self._snapshot.send(identity, zmq.SNDMORE)  # @UndefinedVariable
                self._snapshot.send(b'KTHXBAI')
    
        print(" Interrupted\n%d messages handled" % sequence)


if __name__ == '__main__':
    server = Server()
    server.run()
