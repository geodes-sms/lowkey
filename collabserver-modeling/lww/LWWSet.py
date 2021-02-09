#!/usr/bin/env python
__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWSet data type with a built-in SetElement.
Based on the LWW-element-Set specification in https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.
"""


class SetElement(): 

    def __init__(self, value, timestamp):
        self.__value = value
        self.__timestamp = timestamp
        self.__deleted = False
        
    def getValue(self):
        return self.__value
    
    def remove(self, timestamp):
        self.__deleted = True
        self.__timestamp = timestamp
        
    def isDeleted(self):
        return self.__deleted


class LWWSet():
    
    def __init__(self):
        self.__elements = set()
        self.__timestamp = 0
    
    def query(self, element) -> bool:
        if self.__find(element):
            return True
        return False

    def __find(self, element) -> SetElement:
        return next((e for e in self.__elements if e.getValue() == element and not e.isDeleted()), None)

    def add(self, element, timestamp: int):
        if not self.query(element):
            self.__addElement(element, timestamp)
            self.__timestamp = timestamp

    def __addElement(self, element, timestamp):
        self.__elements.add(SetElement(element, timestamp))

    def remove(self, element, timestamp: int):
        if self.query(element):
            self.__removeElement(element, timestamp)
            self.__timestamp = timestamp
    
    def __removeElement(self, element, timestamp):
        element = self.__find(element)
        if element:
            element.remove(timestamp)
    
    def clear(self, timestamp: int):
        [e.remove(timestamp) for e in self.__elements]
            
    def size(self) -> int:
        return len([x for x in self.__elements if not x.isDeleted()])
    
    def merge(self, otherSet):
        pass