#!/usr/bin/env python
import uuid

from lww import LWWRegister

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWRegister data type.
Based on Specification 9 in https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.
"""


class LWWRegister():
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, LWWRegister):
            return self.__id == other.getId()
        return False
    
    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))
    
    def __init__(self, value=None, timestamp:int=0, prototype:LWWRegister=None):
        self.__id = prototype.getId() if prototype else uuid.uuid1()
        self.__value = value
        self.__timestamp = timestamp
    
    def query(self):
        return self.__value
    
    def update(self, newValue, timestamp: int):
        if timestamp > self.__timestamp:
            self.__value = newValue
            self.__timestamp = timestamp
    
    def getTimestamp(self):
        return self.__timestamp
    
    def getId(self):
        return self.__id
