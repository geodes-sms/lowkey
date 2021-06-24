#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""

"""
Clone server Model One

"""

import time

import zmq


def main():
    # Prepare our context and publisher socket
    ctx = zmq.Context()
    publisher = ctx.socket(zmq.PUB)  # @UndefinedVariable

    publisher.bind("tcp://*:5556")
    # time.sleep(0.2)
    
    sequence = 0
    # random.seed(time.time())
    # kvmap = {}
    
    print("Start loop from %i" % sequence)

    try:
        while True:
            # Distribute as key-value message
            sequence += 1
            # kvmsg = KVMsg(sequence)
            # kvmsg.key = "%d" % random.randint(1, 10000)
            # kvmsg.body = "%d" % random.randint(1, 1000000)
            # kvmsg.send(publisher)
            # kvmsg.store(kvmap)
            msg = "Message: %i" % sequence
            print("Sending message: '%s'" % msg)
            publisher.send_string(msg)
            time.sleep(1) 
            
    except KeyboardInterrupt:
        print(" Interrupted\n%d messages out" % sequence)


if __name__ == '__main__':
    main()
