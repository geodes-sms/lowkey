#!/usr/bin/env python
import logging
import sys

from zmq import Context
import zmq

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Subscriber facility for clients.
"""


class Subscriber:

    def __init__(self, address="127.0.0.1", port="5567", loggingLevel=logging.DEBUG):
        logging.basicConfig()
        logging.getLogger().setLevel(loggingLevel)
        
        self.context = Context.instance()
        self.url = "tcp://{}:{}".format(address, port)
        
        logging.info("Initializing subscriber.")
        
        self.sub = self.context.socket(zmq.SUB)  # @UndefinedVariable
        self.sub.connect(self.url)
        
        self.__topic = ""
        self.sub.setsockopt(zmq.SUBSCRIBE, self.__topic.encode("ascii"))  # @UndefinedVariable
        
        self.listen()

    def listen(self):
        logging.info("Subscriber listening.")
        while True:
            try:
                msg_received = self.sub.recv()
                print("sub: {}".format(msg_received.decode("ascii")))
            except zmq.Again:
                pass


if __name__ == "__main__":
    logging.info("Running with arguments: {}.".format(sys.argv))
    Subscriber()
