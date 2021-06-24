#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""

import zmq

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.REQ)  # @UndefinedVariable
socket.connect("tcp://localhost:5559")

#  Do 10 requests, waiting each time for a response
for request in range(1, 11):
    socket.send(b"Hello")
    message = socket.recv()
    print(f"Received reply {request} [{message}]")
