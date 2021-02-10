#!/usr/bin/env python
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
    
    def query(self, value) -> bool:
        return True if self.__findByValue(value) else False
    
    def __findByValue(self, value) -> LWWRegister:
        a = self.__findLatestInAddSet(value)
        
        if not a:
            return None
        
        return a if self.__exists(a) else None
        
    def __findLatestInAddSet(self, value):
        addSetOccurrences = self.__findInAddSet(value)
        return self.__orderByTimestamp(addSetOccurrences)[0] if addSetOccurrences else None
    
    def __findLatestInRemoveSet(self, value):
        removeSetOccurrences = self.__findInRemoveSet(value)
        return self.__orderByTimestamp(removeSetOccurrences)[0] if removeSetOccurrences else None

    def __findInAddSet(self, value):
        return self.__findInInternalSet(value, self.__addSet)
    
    def __findInRemoveSet(self, value):
        return self.__findInInternalSet(value, self.__removeSet)
    
    def __findInInternalSet(self, value, _set):
        return [a for a in _set if a.query() == value]
    
    def __orderByTimestamp(self, setElementCollection):

        def timestamp(elem):
            return elem.getTimestamp()
        
        return sorted(setElementCollection, key=timestamp, reverse=True)

    def add(self, element, timestamp: int):
        if not self.query(element):
            self.__addElement(element, timestamp)

    def __addElement(self, element, timestamp):
        self.__addSet.add(LWWRegister(element, timestamp))
    
    def remove(self, element, timestamp: int):
        if self.query(element):
            self.__removeElement(element, timestamp)
    
    def __removeElement(self, element, timestamp):
        self.__removeSet.add(LWWRegister(element, timestamp))
        
    def clear(self, timestamp: int):
        [self.__removeElement(a.query(), timestamp) for a in self.__addSet if self.__exists(a)]
                
    def __exists(self, element):
        return True if self.__noEffectiveRemoveExists(element) else False
    
    def __noEffectiveRemoveExists(self, latestAddOfElement):
        latestRemoveOfElement = self.__findLatestInRemoveSet(latestAddOfElement.query())
        
        return (not latestRemoveOfElement or latestRemoveOfElement.getTimestamp() < latestAddOfElement.getTimestamp())
    
    def size(self) -> int:
        return sum(self.__exists(a) for a in self.__addSet)
    
    """TODO: def __iter__(self):"""
    """TODO:"""
    def merge(self, otherSet):
        pass