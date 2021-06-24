#!/usr/bin/env python
import time

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""

import random

import zmq


def consumer():
    consumer_id = random.randrange(1, 10005)
    print("I am consumer #%s" % (consumer_id))
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)  # @UndefinedVariable
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    # send work
    consumer_sender = context.socket(zmq.PUSH)  # @UndefinedVariable
    consumer_sender.connect("tcp://127.0.0.1:5558")
    
    while True:
        work = consumer_receiver.recv_json()
        #data = work['num']
        print(work)
        time.sleep(1000)

consumer()
