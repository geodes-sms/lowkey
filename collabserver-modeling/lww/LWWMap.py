#!/usr/bin/env python
from lww.LWWRegister import LWWRegister
from lww.LWWSet import LWWSet

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWMap data type.
Loosely based on the specification https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.
"""


class Mapping():

    def __init__(self, key, value, timestamp):
        self.__key:LWWRegister = key
        self.__value:LWWRegister = LWWRegister(value, timestamp)
        
    def getKey(self):
        return self.__key.query()
    
    def getValue(self):
        return self.__value.query()
    
    def getTimestamp(self):
        return self.getValue().getTimestamp()


class LWWMap():
    
    def __init__(self):
        self.__keySet = LWWSet()
        self.__mappings = set()
    
    """Interface methods"""
    
    def query(self, key):
        mapping = None
        
        if self.__keySet.query(key):
            for m in self.__mappings:
                if m.getKey() == key:
                    mapping = m
                    break
        
        if mapping:
            return mapping.getValue()
        return None
    
    def add(self, key, value, timestamp: int):
        added = self.__keySet.add(key, timestamp)
        
        if added:
            self.__mappings.add(Mapping(self.__keySet.lookup(key), value, timestamp))
    
    def remove(self, key, timestamp: int):
        currentMapping = self.__lookupMapping(key)
        
        if currentMapping:
            self.__mappings.remove(currentMapping)
        self.__keySet.remove(key, timestamp)
    
    def update(self, key, newValue, timestamp):
        currentMapping = self.__lookupMapping(key)
        
        if currentMapping:
            self.__mappings.remove(currentMapping)
            self.__mappings.add(Mapping(self.__keySet.lookup(key), newValue, timestamp))
                    
    def clear(self, timestamp: int):
        pass
    
    def size(self):
        return self.__keySet.size()
    
    """Internal methods"""

    def __lookupMapping(self, key):
        mapping = None
        
        if self.__keySet.query(key):
            for m in self.__mappings:
                if m.getKey() == key:
                    mapping = m
                    break
        
        return mapping
