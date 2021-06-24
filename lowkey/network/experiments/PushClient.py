#!/usr/bin/env python
import time

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""

import zmq


def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)  # @UndefinedVariable
    zmq_socket.bind("tcp://127.0.0.1:5557")
    # Start your result manager and workers before you start your producers
    for num in range(20000):
        work_message = { 'num': num }
        print(work_message)
        zmq_socket.send_json(work_message)
        time.sleep(1000)

producer()
