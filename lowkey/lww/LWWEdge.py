#!/usr/bin/env python
from lww.LWWMap import LWWMap
from lww.LWWVertex import LWWVertex

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWEdge for representing edges in LWWGraphs.
"""


class LWWEdge(LWWMap):

    def __init__(self):
        super().__init__()

    def setFrom(self, vertex:LWWVertex, timestamp):
        self.add("from", vertex, timestamp)
        
    def setTo(self, vertex:LWWVertex, timestamp):
        self.add("to", vertex, timestamp)
