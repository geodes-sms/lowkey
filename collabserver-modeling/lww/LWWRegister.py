#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWRegister data type.
Based on Specification 9 in https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.
"""


class LWWRegister():
    
    def __init__(self, value=None, timestamp=0):
        self.value = value
        self.timestamp = timestamp
        
    def query(self):
        return self.value
    
    def update(self, newValue, timestamp: int):
        if timestamp > self.timestamp:
            self.value = newValue
            self.timestamp = timestamp
            
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, LWWRegister):
            return self.value == other.query()
        
    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))
