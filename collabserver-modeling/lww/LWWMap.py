#!/usr/bin/env python
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
        self.__key = key
        self.__value = value
        self.__timestamp = timestamp
        
    def getKey(self):
        return self.__key
    
    def getValue(self):
        return self.__value


class LWWMap():
    
    def __init__(self):
        self.__keySet = LWWSet()
        self.__values = list()
        self.__mappings = list()
    
    def query(self, key):
        if key in self.__keySet:
            for m in self.__mappings:
                if m.getKey() == key:
                    return m.getValue()
            
        return None
    
    def add(self, key, value, timestamp: int):
        if key in self.__keySet:
            return
        
        self.__keySet.add(key, timestamp)
        self.__values.append(value)
        self.__mappings.append(Mapping(key, value, timestamp))
    
    def remove(self, key, timestamp: int):
        value = self.query(key)
        if value:
            self.__keySet.remove(key, timestamp)
            self.__values.remove(value)
            
            mapping = None
            
            for m in self.__mappings:
                if m.getKey() == key:
                    mapping = m
                    break
            
            if mapping:
                self.__mappings.remove(mapping)
    
    def clear(self, timestamp: int):
        pass
