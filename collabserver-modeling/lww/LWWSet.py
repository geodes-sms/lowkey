#!/usr/bin/env python
from typing import List

from lww.LWWRegister import LWWRegister

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWSet data type with a built-in SetElement.
Based on the LWW-element-Set specification in https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.
"""


class LWWSet():
    
    def __init__(self):
        self.__addSet = set()
        self.__removeSet = set()
    
    """TODO: def __iter__(self):"""
    
    """Interface methods"""

    def query(self, value) -> bool:
        return True if self.__lookup(value) else False
    
    def add(self, value, timestamp: int):
        """We really have to use this one here instead of
        a = self.__findInAddSetSortByDescendingTimestamp(value). By doing so, we allow potentially
        duplicated A-entries, but we account for potentially late R-entries invalidating an older
        A-entry.
        The only catch is, that lookup(value) should interpret duplicated A-entries as one masking
        the other, and only the latest shall be interpreted as existing.
        """
        a = self.__lookup(value)
        
        if not a or a.getTimestamp() < timestamp:
            self.__addRegisterWithValue(value, timestamp)
            
    def remove(self, value, timestamp: int):
        self.__removeRegisterWithValue(value, timestamp)
    
    def clear(self, timestamp: int):
        for a in self.__addSet:
            if not self.__removeExistsForRegister(a):
                self.__removeRegister(a, timestamp)
    
    def size(self) -> int:
        counted = set()
        for a in self.__addSet:
            if not self.__removeExistsForRegister(a):
                counted.add(a.getValue())
        return len(counted)
    
    def merge(self, otherSet):  # TODO
        pass
    
    """Internal methods"""

    def __lookup(self, value) -> LWWRegister:
        for a in self.__findInAddSetSortByDescendingTimestamp(value):  # TODO this should be solved by the LWWStack
            if not self.__removeExistsForRegister(a):
                return a

        return None

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
        self.__addSet.add(LWWRegister(value, timestamp, prototype))
    
    def __removeRegisterWithValue(self, value, timestamp):
        self.__removeSet.add(LWWRegister(value, timestamp, self.__lookup(value)))
        
    def __removeRegister(self, aRegister, timestamp):
        self.__removeSet.add(LWWRegister(timestamp=timestamp, prototype=aRegister))
