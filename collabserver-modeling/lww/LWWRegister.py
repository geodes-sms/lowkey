#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWRegister data type.
Loosely based on the specification https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.
"""


class LWWRegister():
    
    def __init__(self):
        self.__value = None
        self.__timestamp = 0
    
    def query(self):
        return self.__value
    
    def update(self, newValue, timestamp: int):
        if timestamp > self.__timestamp:
            self.__value = newValue
            self.__timestamp = timestamp