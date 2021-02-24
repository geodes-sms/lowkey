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

Extends the LWWSet type. The keySet is an LWWSet, and a set Mappings is used to link values to the
keys. For each key, there is one mapping, which holds (i) a reference to the key, (ii) the value, and
(iii) a timestamp. The construct is augmented with CRDT semantics by the keySet's LWWSet.
"""


class Mapping():

    def __init__(self, key, value, timestamp):
        self.__keyRegister:LWWRegister = key
        self.__valueRegister:LWWRegister = LWWRegister(value, timestamp)
    
    def getKey(self):
        return self.__keyRegister.query()
    
    def getKeyRegister(self):
        return self.__keyRegister
    
    def getValue(self):
        return self.__valueRegister.query()
    
    def getValueRegister(self):
        return self.__valueRegister
    
    def getTimestamp(self):
        return self.__valueRegister.getTimestamp()


class LWWMap():
    
    def __init__(self):
        self.__keySet = LWWSet()
        self.__mappings = set()
    
    """Interface methods"""
    
    def query(self, key):
        mapping = self.__lookupMapping(key)
        
        if mapping:
            return mapping.getValue()
        return None
    
    def exists(self, key):
        return True if self.__lookupMapping(key) else False
    
    def add(self, key, value, timestamp: int):
        newKeyRegister = self.__keySet.add(key, timestamp)
        
        if newKeyRegister:
            self.__mappings.add(Mapping(newKeyRegister, value, timestamp))
    
    def remove(self, key, timestamp: int):
        currentMapping = self.__lookupMapping(key)
        
        if not currentMapping:
            raise KeyError  # this would mean an earlier value insertion/removal discrepancy
        
        self.__mappings.remove(currentMapping)
        self.__keySet.remove(key, timestamp)
    
    """
    Update is not supported currently, as it requires further formal analysis regarding its preservation
    of CTRD consistency properties.
    """
    """
    def update(self, key, newValue, timestamp):
        currentMapping = self.__lookupMapping(key)
        
        if not currentMapping:
            raise KeyError  # this would mean an earlier value insertion/removal discrepancy
            
        self.__mappings.remove(currentMapping)
        self.__mappings.add(Mapping(self.__keySet.lookup(key), newValue, timestamp))
    """
                    
    def clear(self, timestamp: int):
        pass
    
    def size(self):
        return self.__keySet.size()
    
    """Internal methods""" 
    
    def __lookupMappingsForKey(self, key):
        mappings = set()
        
        for m in self.__mappings:
            if m.getKey() == key:
                mappings.add(m)
    
        return mappings
    
    def __latestMappingForKey(self, key):
        mapping = None
        
        for m in self.__lookupMappingsForKey(key):
            if not mapping or mapping.getTimestamp() < m.getTimestamp():
                mapping = m
                
        return mapping
    
    def __lookupMapping(self, key):
        mapping = self.__latestMappingForKey(key)
        
        return mapping
