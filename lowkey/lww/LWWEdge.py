#!/usr/bin/env python
from lowkey.lww.LWWMap import LWWMap

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
