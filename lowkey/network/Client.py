#!/usr/bin/env python
import logging
import os
import sys
import time
import uuid

import zmq

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from network.LWWAwareComponent import LWWAwareComponent 

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Generic client component.
"""


class Client(LWWAwareComponent):

    def __init__(self):
        self._id = uuid.uuid1()
        
        ctx = zmq.Context()
        
        self._snapshot = ctx.socket(zmq.DEALER)
        self._snapshot.linger = 0
        self._snapshot.connect("tcp://localhost:5556")
        self._subscriber = ctx.socket(zmq.SUB)
        self._subscriber.linger = 0
        self._subscriber.subscribe("")
        self._subscriber.connect("tcp://localhost:5557")
        self._publisher = ctx.socket(zmq.PUSH)
        self._publisher.linger = 0
        self._publisher.connect("tcp://localhost:5558")
        
        self._poller = zmq.Poller()
        self._poller.register(self._subscriber, zmq.POLLIN)

    def join(self):
        self._snapshot.send(b"request_snapshot")
        while True:
            try:
                message = self._snapshot.recv()
                logging.debug(message)
            except:
                return  # Interrupted
            if message == b"finished_snapshot":
                # sequence = kvmsg.sequence
                logging.debug("Received snapshot")
                break  # Done

    def subscribe(self):
        logging.debug("Receiving messages")
        
        alarm = time.time() + 1.
        while True:
            tickless = 1000 * max(0, alarm - time.time())
            try:
                items = dict(self._poller.poll(tickless))
            except:
                break  # Interrupted
    
            if self._subscriber in items:
                self.subscriberAction()
    
            if time.time() >= alarm:
                self.timeoutAction()
    
        logging.debug("Interrupted")
        
    def subscriberAction(self):
        raise NotImplementedError
    
    def timeoutAction(self):
        raise NotImplementedError
