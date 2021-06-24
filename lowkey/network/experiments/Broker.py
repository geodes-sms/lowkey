#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""

import zmq

# Prepare our context and sockets
context = zmq.Context()
frontend = context.socket(zmq.ROUTER)  #  @UndefinedVariable
backend = context.socket(zmq.DEALER)  #  @UndefinedVariable
frontend.bind("tcp://*:5559")
backend.bind("tcp://*:5560")

# Initialize poll set
poller = zmq.Poller()
poller.register(frontend, zmq.POLLIN)  #  @UndefinedVariable
poller.register(backend, zmq.POLLIN)  #  @UndefinedVariable

# Switch messages between sockets
while True:
    socks = dict(poller.poll())

    if socks.get(frontend) == zmq.POLLIN:  #  @UndefinedVariable
        message = frontend.recv_multipart()
        backend.send_multipart(message)

    if socks.get(backend) == zmq.POLLIN:  #  @UndefinedVariable
        message = backend.recv_multipart()
        frontend.send_multipart(message)
