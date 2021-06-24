#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""

import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)  #  @UndefinedVariable
socket.connect("tcp://localhost:5560")

while True:
    message = socket.recv()
    print(f"Received request: {message}")
    socket.send(b"World")
