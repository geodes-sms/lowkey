#!/usr/bin/env python
from lww import LWWPlainValueMap
from lww.LWWPlainValueSet import LWWPlainValueSet

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWMap data type.
Loosely based on the specification https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.

Extends the LWWSet type.
"""


class ViewSet():
    
    def __init__(self, lwwMap:LWWPlainValueMap):
        self._lwwMap = lwwMap
        
    def _collectViewElements(self):
        raise NotImplementedError
        
    def __iter__(self):
        self._collectViewElements()
        self.__currentIteratorIndex = len(self._viewElements)
        return self

    def __next__(self):
        if self.__currentIteratorIndex > 0:
            self.__currentIteratorIndex -= 1
            viewElement = self._viewElements[self.__currentIteratorIndex]
            return viewElement 
        else: 
            raise StopIteration


class EntrySet(ViewSet):

    def __init__(self, lwwMap:LWWPlainValueMap):
        super().__init__(lwwMap)
            
    def _collectViewElements(self):
        self._viewElements = list()
        for (key, value), timestamp in self._lwwMap._existing():
            self._viewElements.append(((key, value), timestamp))


class KeySet(ViewSet):

    def __init__(self, lwwMap:LWWPlainValueMap):
        super().__init__(lwwMap)
            
    def _collectViewElements(self):
        self._viewElements = list()
        for (key, _), _ in self._lwwMap._existing():
            self._viewElements.append(key)


class LWWPlainValueMap(LWWPlainValueSet):

    def __init__(self):
        super().__init__()
    
    """Getters"""
    
    def keySet(self):
        return KeySet(self)
    
    def entrySet(self):
        return EntrySet(self)
    
    """Interface methods"""
    
    def _lookupFunction(self, entry):
        return entry[0][0]
    
    def _getValue(self, entry):
        return entry[0][1]
    
    def _getTimestamp(self, entry):
        return entry[1]
    
    def query(self, key):
        query = next((entry for entry in self._existing() if self._lookupFunction(entry) == key), None)
        return self._getValue(query) if query else None
    
    def lookup(self, key) -> bool:
        return super().lookup(key)
    
    def add(self, key, value, timestamp: int) -> bool:
        if any(key == self._lookupFunction(addedValue) and timestamp < self._getTimestamp(addedValue) for addedValue in self._addSet):  # LWW
            return False
        
        self._addSet.add(((key, value), timestamp))
        return True
    
    def remove(self, key, timestamp: int):
        if any(key == self._lookupFunction(removedValue) and timestamp < self._getTimestamp(removedValue) for removedValue in self._removeSet):  # LWW
            return False
        self._removeSet.add(((key, self.query(key)), timestamp))
    
    def update(self, key, newValue, timestamp):
        raise NotImplementedError
                    
    def clear(self, timestamp: int):
        if(self.size() == 0):
            return
        
        for (key, value), _ in self._existing():
            self.remove((key, value), timestamp)
    
    def _existing(self):
        if len(self._addSet) == 0:
            return list()
        
        keyFunc = lambda x: self._getTimestamp(x)
        # sorting in descending order to start with the likely existing ones and short-circuit the loop below
        addedEntries = sorted(self._addSet, key=keyFunc, reverse=True)
        
        existing = list()
        for (key, value), timestamp in addedEntries:
            existingEntry = next(iter([entry for entry in existing if self._lookupFunction(entry) == key]), None)
            
            if not existingEntry:
                if not self._laterRemoveExists(key, timestamp):
                    existing.append(((key, value), timestamp))
                    continue
            elif self._getTimestamp(existingEntry) < timestamp:
                existing.remove(existingEntry)
                existing.append(((key, value), timestamp))
            else:
                continue
                
        return existing
    
    def _laterRemoveExists(self, key, timestamp):
        if not any(key == self._lookupFunction(removedValue) for removedValue in self._removeSet):
            return False
        
        lastRemoved = max(self._getTimestamp(entry) for entry in self._removeSet if key == self._lookupFunction(entry))
        
        return timestamp < lastRemoved
