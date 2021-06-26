#!/usr/bin/env python
import os
import sys

import zmq
import logging
import argparse

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from network.Memory import Memory

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Server component, responsible for:
-publishing the initial snapshot to joiners (via ROUTER/DEALER);
-pulling client updates (via PULL/PUSH);
-distributing client updates (via PUB/SUB).
"""


class Server():
    
    def __init__(self):
        ctx = zmq.Context()
        
        self._snapshot = ctx.socket(zmq.ROUTER)
        self._snapshot.bind("tcp://*:5556")
        self._publisher = ctx.socket(zmq.PUB)
        self._publisher.bind("tcp://*:5557")
        self._collector = ctx.socket(zmq.PULL)
        self._collector.bind("tcp://*:5558")
        
        self._poller = zmq.Poller()
        self._poller.register(self._collector, zmq.POLLIN)
        self._poller.register(self._snapshot, zmq.POLLIN)
        
        self._memory = Memory()
    
    def run(self):
        while True:
            try:
                items = dict(self._poller.poll(1000))
            except:
                break
            
            # PULLed messages PUBLISHED by the clients
            if self._collector in items:
                message = self._collector.recv()
                logging.debug("Saving message: {}".format(message))
                self._memory.saveMessage(message)
                logging.debug("Publishing update")
                self._publisher.send(message)
            
            # snapshot requests by joining clients
            if self._snapshot in items:
                message = self._snapshot.recv_multipart()
                identity = message[0]
                request = message[1]
                logging.debug("Identity: {}".format(identity))
                logging.debug("Request: {}".format(request))
                if request == b"request_snapshot":
                    pass
                else:
                    print("Bad request, aborting.")
                    break
    
                for message in self._memory.getMessages():
                    self._snapshot.send(identity, zmq.SNDMORE)
                    logging.debug("Sending message {}".format(message))
                    self._snapshot.send(message)
    
                logging.debug("Sent state shapshot")
                self._snapshot.send(identity, zmq.SNDMORE)
                self._snapshot.send(b'finished_snapshot')
    
        print("Interrupted")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-log",
        "--log",
        default="warning",
        help=("Provide logging level. "
              "Example '--log debug', default='warning'."
              )
        )

    options = parser.parse_args()
    levels = {
        'critical': logging.CRITICAL,
        'error': logging.ERROR,
        'warn': logging.WARNING,
        'warning': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG
    }
    level = levels.get(options.log.lower())
    if level is None:
        raise ValueError(
            f"log level given: {options.log}"
            f" -- must be one of: {' | '.join(levels.keys())}")
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=level)
    
    server = Server()
    server.run()
