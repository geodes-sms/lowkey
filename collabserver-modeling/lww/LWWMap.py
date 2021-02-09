#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWMap data type.
Loosely based on the specification https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.
"""


class LWWMap():
    
    def __init__(self):
        pass
    
    def query(self, key):
        pass
    
    def add(self, key, value, timestamp: int):
        pass
    
    def remove(self, key, timestamp: int):
        pass
    
    def clear(self, timestamp: int):
        pass