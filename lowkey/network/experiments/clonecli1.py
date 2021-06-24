#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""

"""
Clone Client Model One

Author: Min RK <benjaminrk@gmail.com>

"""

import zmq


def main():
    # Prepare our context and publisher socket
    ctx = zmq.Context()
    updates = ctx.socket(zmq.SUB)  # @UndefinedVariable
    #updates.linger = 0
    #updates.setsockopt_string(zmq.SUBSCRIBE, '')  # @UndefinedVariable
    updates.subscribe("")
    updates.connect("tcp://localhost:5556")

    #kvmap = {}
    sequence = 0
    msg = ""
    
    print("Start receiving updates")

    while True:
        try:
            #kvmsg = KVMsg.recv_string(updates)
            msg = updates.recv_string()
        except:
            break  # Interrupted
        #kvmsg.store(kvmap)
        #sequence += 1
        print(msg)
    print("Interrupted\n%d messages in" % sequence)


if __name__ == '__main__':
    main()
