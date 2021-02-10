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

'''
class SetElement(): 

    def __init__(self, value, timestamp):
        self.value = value
        self.timestamp = timestamp
        
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, SetElement):
            return self.value == other.value
        
    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))
'''


class LWWSet():
    
    def __init__(self):
        self.__addSet = set()
        self.__removeSet = set()
    
    def query(self, value) -> bool:
        if self.__findByValue(value):
            return True
        return False
    
    def __findByValue(self, value) -> LWWRegister:
        a = self.__findLatestInAddSet(value)
        
        if not a:
            return None
        
        r = self.__findLatestInRemoveSet(value)
        
        if self.__noEffectiveRemoveExists(a, r):
            return a
        
        return None
        
    def __findLatestInAddSet(self, value):
        addSetOccurrences = self.__findInAddSet(value)
        if not addSetOccurrences:
            return None
        
        return self.__orderByTimestamp(addSetOccurrences)[0]
    
    def __findLatestInRemoveSet(self, value):
        removeSetOccurrences = self.__findInRemoveSet(value)
        if not removeSetOccurrences:
            return None
        
        return self.__orderByTimestamp(removeSetOccurrences)[0]

    def __findInAddSet(self, value):
        return self.__findInInternalSet(value, self.__addSet)
    
    def __findInRemoveSet(self, value):
        return self.__findInInternalSet(value, self.__removeSet)
    
    def __findInInternalSet(self, value, _set):
        return [a for a in _set if a.value == value]
    
    def __orderByTimestamp(self, setElementCollection):

        def timestamp(elem):
            return elem.timestamp
        
        return sorted(setElementCollection, key=timestamp, reverse=True)

    def __noEffectiveRemoveExists(self, latestAddOfElement, latetsRemoveOfElement):
        return (not latetsRemoveOfElement or latetsRemoveOfElement.timestamp < latestAddOfElement.timestamp)
    
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
        for a in self.__addSet:
            if self.__exists(a):
                self.__removeElement(a.value, timestamp)
        
    def __exists(self, element):
        r = self.__findLatestInRemoveSet(element.value)
        if self.__noEffectiveRemoveExists(element, r):
            return True
        return False
    
    def size(self) -> int:
        size = 0
        for a in self.__addSet:
            if self.__exists(a):
                size += 1
        return size
   
    def merge(self, otherSet):
        pass
