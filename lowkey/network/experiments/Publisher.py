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
Publisher facility for clients.
"""


class Publisher:

    def __init__(self, address="127.0.0.1", port="5566"):
        self.context = Context.instance()
        self.url = "tcp://{}:{}".format(address, port)
        
        logging.info("Initializing publisher at URL {}.".format(self.url))
        
        self.pub = self.context.socket(zmq.PUB)  # @UndefinedVariable
        self.pub.connect(self.url)
        
        self.__topic = ""

    def sendMessage(self, message): 
        logging.info("Message to be published: {}".format(message))

        self.pub.send(message.encode("ascii"))
        
        logging.info("Message published.".format(message))

    
    def sendJSONMessage(self, jsonMessage):
        logging.info("Message to be published.")

        self.pub.send_json(jsonMessage.encode("ascii"))
        
        logging.info("Message published.")
    
    


if __name__ == "__main__":
    logging.info("Running with arguments: {}.".format(sys.argv))
    Publisher()
