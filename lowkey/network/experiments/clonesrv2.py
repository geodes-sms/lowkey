#!/usr/bin/env python
import os
import sys
import threading
import time

import zmq

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from network.zhelpers import zpipe

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""

"""
Clone server Model One

"""


def main():
    ctx = zmq.Context()
    publisher = ctx.socket(zmq.PUB)  # @UndefinedVariable
    publisher.bind("tcp://*:5556")
    time.sleep(0.2)  # Late joiners
    
    sequence = 0
    memory = Memory()
    
    updates, peer = zpipe(ctx)

    manager_thread = threading.Thread(target=state_manager, args=(ctx, peer, memory))

    manager_thread.daemon = True
    print("Starting state manager thread")
    manager_thread.start()
    
    print("Start loop from %i" % sequence)

    try:
        while True:
            sequence += 1
            memory.append(sequence)
            # kvmsg = KVMsg(sequence)
            # kvmsg.key = "%d" % random.randint(1, 10000)
            # kvmsg.body = "%d" % random.randint(1, 1000000)
            # kvmsg.send(publisher)
            # kvmsg.store(kvmap)
            msg = "Message: %i" % sequence
            print("Sending message: '%s'" % msg)
            print("Memory: {}.".format(memory._memory))
            publisher.send_string(msg)
            time.sleep(1) 
            
    except KeyboardInterrupt:
        print(" Interrupted\n%d messages out" % sequence)


class Memory:

    def __init__(self):
        self._memory = []
        
    def append(self, data):
        self._memory.append(data)
        
# simple struct for routing information for a key-value snapshot
class Route:

    def __init__(self, socket, identity):
        self.socket = socket  # ROUTER socket to send to
        self.identity = identity  # Identity of peer who requested state


def send_single(route, data):
    """Send one state snapshot key-value pair to a socket

    Hash item data is our kvmsg object, ready to send
    """
    # Send identity of recipient first
    route.socket.send(route.identity, zmq.SNDMORE)  # @UndefinedVariable
    route.socket.send(data)
    # kvmsg.send(route.socket)


def state_manager(ctx, pipe, memory):
    """This thread maintains the state and handles requests from clients for snapshots.
    """
    # kvmap = {}
    pipe.send_string("READY")
    snapshot = ctx.socket(zmq.ROUTER)  # @UndefinedVariable
    snapshot.bind("tcp://*:5557")

    poller = zmq.Poller()
    poller.register(pipe, zmq.POLLIN)  # @UndefinedVariable
    poller.register(snapshot, zmq.POLLIN)  # @UndefinedVariable

    sequence = 0  # Current snapshot version number
    while True:
        try:
            items = dict(poller.poll())
        except (zmq.ZMQError, KeyboardInterrupt):
            break  # interrupt/context shutdown

        # Apply state update from main thread
        if pipe in items:
            msg = pipe.recv_string()
            print(msg)
            # kvmsg = KVMsg.recv(pipe)
            # sequence = kvmsg.sequence
            # kvmsg.store(kvmap)
        # Execute state snapshot request
        if snapshot in items:
            msg = snapshot.recv_multipart()
            identity = msg[0]
            request = msg[1]
            if request == b"ICANHAZ?":
                print("Identity: {}".format(identity))
                print("Request: {}".format(request))
                print("You can have")
            else:
                print("E: bad request, aborting\n")
                break
            # Send state snapshot to client
            route = Route(snapshot, identity)

            # For each entry in kvmap, send kvmsg to client
            # for k,v in kvmap.items():
            
            #send_single(route)

            # Now send END message with sequence number
            print("Sending state shapshot")
            snapshot.send(identity, zmq.SNDMORE)  # @UndefinedVariable
            
            #memLen = len(memory._memory)
            #for i in range(4):
            #    send_single(route,i)  # @UndefinedVariable
            
            # kvmsg = KVMsg(sequence)
            # kvmsg.key = "KTHXBAI"
            # kvmsg.body = ""
            # kvmsg.send(snapshot)
            #snapshot.send(b"some message", zmq.SNDMORE) # @UndefinedVariable
            
            snapshot.send(b"KTHXBAI")


if __name__ == '__main__':
    main()
