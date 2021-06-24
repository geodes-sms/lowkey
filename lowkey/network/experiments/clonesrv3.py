#!/usr/bin/env python
import sys
import os

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Clone server Model Three

Author: Min RK <benjaminrk@gmail.com
"""

import zmq

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from network.kvsimple import KVMsg


# simple struct for routing information for a key-value snapshot
class Route:

    def __init__(self, socket, identity):
        self.socket = socket  # ROUTER socket to send to
        self.identity = identity  # Identity of peer who requested state


def send_single(key, kvmsg, route):
    """Send one state snapshot key-value pair to a socket"""
    # Send identity of recipient first
    route.socket.send(route.identity, zmq.SNDMORE)  # @UndefinedVariable
    kvmsg.send(route.socket)


def main():
    # context and sockets
    ctx = zmq.Context()
    snapshot = ctx.socket(zmq.ROUTER)  # @UndefinedVariable
    snapshot.bind("tcp://*:5556")
    publisher = ctx.socket(zmq.PUB)  # @UndefinedVariable
    publisher.bind("tcp://*:5557")
    collector = ctx.socket(zmq.PULL)  # @UndefinedVariable
    collector.bind("tcp://*:5558")

    sequence = 0
    #kvmap = {}
    msg = ""

    poller = zmq.Poller()
    poller.register(collector, zmq.POLLIN)  # @UndefinedVariable
    poller.register(snapshot, zmq.POLLIN)  # @UndefinedVariable
    while True:
        try:
            items = dict(poller.poll(1000))
        except:
            break  # Interrupted

        # Apply state update sent from client
        if collector in items:
            #kvmsg = KVMsg.recv(collector)
            msg = collector.recv_string()
            sequence += 1
            #kvmsg.sequence = sequence
            #kvmsg.send(publisher)
            #kvmsg.store(kvmap)
            print("I: publishing update %5d" % sequence)
            publisher.send(b'This was published by the srv.')

        # Execute state snapshot request
        if snapshot in items:
            msg = snapshot.recv_multipart()
            identity = msg[0]
            request = msg[1]
            if request == b"ICANHAZ?":
                pass
            else:
                print("E: bad request, aborting\n")
                break

            # Send state snapshot to client
            route = Route(snapshot, identity)

            # For each entry in kvmap, send kvmsg to client
            #for k, v in kvmap.items():
                #send_single(k, v, route)
            route.socket.send(route.identity, zmq.SNDMORE)  # @UndefinedVariable
            snapshot.send(b'asd')

            # Now send END message with sequence number
            print("Sending state shapshot=%d\n" % sequence)
            snapshot.send(identity, zmq.SNDMORE)  # @UndefinedVariable
            snapshot.send(b'KTHXBAI')
            #kvmsg = KVMsg(sequence)
            #kvmsg.key = "KTHXBAI"
            #kvmsg.body = ""
            #kvmsg.send(snapshot)

    print(" Interrupted\n%d messages handled" % sequence)


if __name__ == '__main__':
    main()
