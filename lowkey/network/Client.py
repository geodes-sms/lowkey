#!/usr/bin/env python
import time

import zmq
import uuid

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class Client():

    def __init__(self):
        self._id = uuid.uuid1()
        
        ctx = zmq.Context()
        
        self._snapshot = ctx.socket(zmq.DEALER)  # @UndefinedVariable
        self._snapshot.linger = 0
        self._snapshot.connect("tcp://localhost:5556")
        self._subscriber = ctx.socket(zmq.SUB)  # @UndefinedVariable
        self._subscriber.linger = 0
        self._subscriber.subscribe("")
        self._subscriber.connect("tcp://localhost:5557")
        self._publisher = ctx.socket(zmq.PUSH)  # @UndefinedVariable
        self._publisher.linger = 0
        self._publisher.connect("tcp://localhost:5558")
        
        self._poller = zmq.Poller()
        self._poller.register(self._subscriber, zmq.POLLIN)  # @UndefinedVariable

    def join(self):
        msg = ""
        self._snapshot.send(b"ICANHAZ?")
        while True:
            try:
                msg = self._snapshot.recv()
                print(msg)
            except:
                return  # Interrupted
            if msg == b"KTHXBAI":
                # sequence = kvmsg.sequence
                print("I: Received snapshot")
                break  # Done
            
    def subscribe(self):
        print("Receiving messages")
        
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
    
        print(" Interrupted")
        
    def subscriberAction(self):
        raise NotImplementedError
    
    def timeoutAction(self):
        raise NotImplementedError
