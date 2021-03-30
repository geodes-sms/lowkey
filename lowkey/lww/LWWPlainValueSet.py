#!/usr/bin/env python
import itertools

_author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWSet data type, based on the LWW-element-Set specification in
https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.

Provides a redundancy-free collection to store values. Values are stored in tuples with their
timestamp. The set emulates the behavior of the standard set types: on its public interface, if a
value exists, only exists once.

The value exists iff:
-there exists an entry in an addSet corresponding to the value, and
---there exists no corresponding entry in the removeSet, or
---there exists a corresponding entry in the removeSet, but with a smaller timestamp.

Otherwise the value does not exist.
"""

    
class LWWPlainValueSet():
            
    def __init__(self):
        self.__addSet = set()
        self.__removeSet = set()
    
    def __iter__(self):
        self.__currentlyExisting = self.__collectExisting()
        self.__currentIteratorIndex = len(self.__currentlyExisting)
        return self

    def __next__(self):
        if self.__currentIteratorIndex > 0:
            self.__currentIteratorIndex -= 1
            element = self.__currentlyExisting[self.__currentIteratorIndex]
            return element
        else: 
            raise StopIteration
    
    """Interface methods"""
    
    def lookup(self, value) -> bool:
        if not any(value == addedValue[0] for addedValue in self.__addSet):
            return False
        if not any(value == removedValue[0] for removedValue in self.__removeSet):
            return True
        
        lastAdded = self.__lastTimestamp(value, self.__addSet)
        lastRemoved = self.__lastTimestamp(value, self.__removeSet)
        
        return lastAdded > lastRemoved
        
    def add(self, newValue, timestamp: int) -> bool:
        if any(newValue == addedValues[0] and timestamp < addedValues[1] for addedValues in self.__addSet):
            return False
        
        self.__addSet.add((newValue, timestamp))
        return True
            
    def remove(self, value, timestamp: int):
        self.__removeSet.add((value, timestamp))
    
    def clear(self, timestamp: int):
        if(self.size() == 0):
            return
        
        existing = self.__collectExisting()
        
        for value, _ in existing:
            self.remove(value, timestamp)
    
    def size(self) -> int:
        if(len(self.__addSet) == 0):
            return 0
        
        return len(list(self.__collectExisting()))
    
    def __lastTimestamp(self, value, entrySet):
        return max(entry[1] for entry in entrySet if value == entry[0])
    
    def __groupEntriesByValue(self, entrySet):
        keyFunc = lambda x: x[0]
        return itertools.groupby(sorted(entrySet, key=keyFunc), keyFunc)
    
    def __collectExisting(self):
        if len(self.__addSet) == 0:
            return list()
        
        existing = list()
        for key, group in self.__groupEntriesByValue(self.__addSet):
            if self.lookup(key):
                lastAdded = self.__lastTimestamp(key, group)
                existing.append((key, lastAdded))
                
        return existing
