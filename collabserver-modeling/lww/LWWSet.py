#!/usr/bin/env python
from typing import List

from lww.LWWRegister import LWWRegister

_author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWSet data type, based on the LWW-element-Set specification in
https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.

Provides a redundancy-free collection to store values. Values are stored in LWWRegisters. The set
emulates the behavior of the standard set types: on its public interface, if a value exists, only
exists once. The following cases can happen:
-there exists no LWWRegister with the value in the addSet: value does not exist in the LWWSet;
-there exists an LWWRegister with the value in the addSet, but
---a corresponding LWWRegister with the same value AND same ID AND greater timestamp exists in
    the remove Set: the value has been deleted, it does not exist;
---a corresponding LWWRegister with the same value AND same ID AND greater timestamp does NOT exist
    in the remove Set: the value has not been deleted, it exists.
"""

    
class LWWSet():
            
    def __init__(self):
        self.__addSet = set()
        self.__removeSet = set()

    def __iter__(self):
        self.__currentlyExisting = self.__lookupExisting()
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
    
    def exists(self, value) -> bool:
        return True if self.lookup(value) else False

    #def query(self, value) -> bool:
    #    return True if self.lookup(value) else False
    
    def add(self, value, timestamp: int) -> bool:
        a = self.lookup(value)
        
        if not a or a.getTimestamp() < timestamp: # recording every add to account for late removals
            register = self.__addRegisterWithValue(value, timestamp)
            return register
        
        return None
            
    def remove(self, value, timestamp: int):
        self.__removeRegisterWithValue(value, timestamp)
    
    def clear(self, timestamp: int):
        for a in self.__addSet:
            if not self.__removeExistsForRegister(a):
                self.__removeRegister(a, timestamp)
    
    def size(self) -> int:
        return len(self.__lookupExisting())
    
    def merge(self, otherSet):  # TODO
        pass
    
    def lookup(self, value) -> LWWRegister:
        for a in self.__findInAddSetSortByDescendingTimestamp(value):
            if not self.__removeExistsForRegister(a):
                return a

        return None
    
    """Internal methods"""
    
    def __lookupExisting(self):
        found = set()  # the set takes care of omitting shadowed values
        for a in self.__addSet:
            if not self.__removeExistsForRegister(a):
                found.add(a.query())
        return list(found)
    
    """
    TODO: This could be more efficient if we used deque instead of set for A and R.
    """

    def __findInAddSetSortByDescendingTimestamp(self, value) -> List[LWWRegister]:
        
        def __orderByTimestamp(setElementCollection):

            def timestamp(elem):
                return elem.getTimestamp()
            
            return sorted(setElementCollection, key=timestamp, reverse=True)
        
        return __orderByTimestamp([a for a in self.__addSet if a.query() == value])
    
    def __removeExistsForRegister(self, a) -> List[LWWRegister]:
        for r in self.__removeSet:
            if r == a and r.getTimestamp() > a.getTimestamp():
                return True
        
        return False

    def __addRegisterWithValue(self, value, timestamp):
        valueInHistory = self.__findInAddSetSortByDescendingTimestamp(value)
        prototype = valueInHistory[0] if valueInHistory else None
        register = LWWRegister(value, timestamp, prototype)
        self.__addSet.add(register)
        return register
    
    def __removeRegisterWithValue(self, value, timestamp):
        self.__removeSet.add(LWWRegister(value, timestamp, self.lookup(value)))
        
    def __removeRegister(self, aRegister, timestamp):
        self.__removeSet.add(LWWRegister(timestamp=timestamp, prototype=aRegister))
