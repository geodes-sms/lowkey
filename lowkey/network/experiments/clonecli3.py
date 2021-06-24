#!/usr/bin/env python
import sys
import os

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Clone client Model Three

Author: Min RK <benjaminrk@gmail.com
"""

import random
import time

import zmq

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from network.kvsimple import KVMsg

def main():

    # Prepare our context and subscriber
    ctx = zmq.Context()
    snapshot = ctx.socket(zmq.DEALER)# @UndefinedVariable
    snapshot.linger = 0
    snapshot.connect("tcp://localhost:5556")
    subscriber = ctx.socket(zmq.SUB)# @UndefinedVariable
    subscriber.linger = 0
    #subscriber.setsockopt(zmq.SUBSCRIBE, '')# @UndefinedVariable
    subscriber.subscribe("")
    subscriber.connect("tcp://localhost:5557")
    publisher = ctx.socket(zmq.PUSH)# @UndefinedVariable
    publisher.linger = 0
    publisher.connect("tcp://localhost:5558")

    random.seed(time.time())
    #kvmap = {}
    msg = ""

    # Get state snapshot
    sequence = 0
    snapshot.send(b"ICANHAZ?")
    while True:
        try:
            #kvmsg = KVMsg.recv(snapshot)
            msg = snapshot.recv()
            print(msg)
        except:
            return          # Interrupted

        if msg == b"KTHXBAI":
            #sequence = kvmsg.sequence
            print("I: Received snapshot")
            break          # Done
        #kvmsg.store(kvmap)

    poller = zmq.Poller()
    poller.register(subscriber, zmq.POLLIN) # @UndefinedVariable
    
    print("Sending / Receiving messages")
    
    alarm = time.time()+1.
    while True:
        tickless = 1000*max(0, alarm - time.time())
        try:
            items = dict(poller.poll(tickless))
        except:
            break           # Interrupted

        if subscriber in items:
            #kvmsg = KVMsg.recv(subscriber)
            msg2 = subscriber.recv()

            # Discard out-of-sequence kvmsgs, incl. heartbeats
            #if kvmsg.sequence > sequence:
            #    sequence = kvmsg.sequence
            #    kvmsg.store(kvmap)
            print("I: received update=%s" % msg2)

        # If we timed-out, generate a random kvmsg
        if time.time() >= alarm:
            #kvmsg = KVMsg(0)
            #kvmsg.key = "%d" % random.randint(1,10000)
            #kvmsg.body = "%d" % random.randint(1,1000000)
            #kvmsg.send(publisher)
            print("Sending message")
            publisher.send(b'sending random data from client')
            #kvmsg.store(kvmap)
            alarm = time.time() + 1.

    print(" Interrupted\n%d messages in" % sequence)

if __name__ == '__main__':
    main()