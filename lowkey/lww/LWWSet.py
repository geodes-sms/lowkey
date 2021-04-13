#!/usr/bin/env python

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

    
class LWWSet():
            
    def __init__(self):
        self._addSet = set()
        self._removeSet = set()
    
    def __iter__(self):
        self.__currentlyExisting = self._existing()
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
        return any(value == self._lookupFunction(existing) for existing in self._existing())
        
    def add(self, newValue, timestamp: int) -> bool:
        if any(newValue == self._lookupFunction(addedValue) and timestamp < self._getTimestamp(addedValue) for addedValue in self._addSet):  # LWW
            return False
        
        self._addSet.add((newValue, timestamp))
        return True
            
    def remove(self, value, timestamp: int):
        if any(value == self._lookupFunction(removedValue) and timestamp < self._getTimestamp(removedValue) for removedValue in self._removeSet):  # LWW
            return False
        self._removeSet.add((value, timestamp))
    
    def clear(self, timestamp: int):
        if(self.size() == 0):
            return
        
        for value, _ in self._existing():
            self.remove(value, timestamp)
    
    def size(self) -> int:
        if(len(self._addSet) == 0):
            return 0
        
        return len(list(self._existing()))
    
    """ Internal methods """

    def _lookupFunction(self, entry):
        return entry[0]
    
    def _getTimestamp(self, entry):
        return entry[1]

    def _existing(self):
        if len(self._addSet) == 0:
            return list()
        
        keyFunc = lambda x: self._getTimestamp(x)
        # sorting in descending order to start with the likely existing ones and short-circuit the loop below
        addedEntries = sorted(self._addSet, key=keyFunc, reverse=True)
        
        existing = list()
        for entry in addedEntries:
            value = self._lookupFunction(entry)
            timestamp = self._getTimestamp(entry)
            existingEntry = next(iter([e for e in existing if self._lookupFunction(e) == value]), None)
            
            if not existingEntry:
                if not self._laterRemoveExists(entry):
                    existing.append(entry)
                    continue
            elif self._getTimestamp(existingEntry) < timestamp:
                existing.remove(existingEntry)
                existing.append(entry)
            else:
                continue
                
        return existing
    
    def _laterRemoveExists(self, entry):
        value = self._lookupFunction(entry)
        timestamp = self._getTimestamp(entry)
        if not any(value == self._lookupFunction(removedValue) for removedValue in self._removeSet):
            return False
        
        lastRemoved = max(self._getTimestamp(e) for e in self._removeSet if value == self._lookupFunction(e))
        
        return timestamp < lastRemoved
