#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""

import pprint

import zmq


def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)  # @UndefinedVariable
    results_receiver.bind("tcp://127.0.0.1:5557")
    collecter_data = {}
    for x in range(1000):
        result = results_receiver.recv_json()
        if collecter_data.has_key(result['consumer']):
            collecter_data[result['consumer']] = collecter_data[result['consumer']] + 1
        else:
            collecter_data[result['consumer']] = 1
        if x == 999:
            pprint.pprint(collecter_data)


result_collector()
