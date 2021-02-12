#!/usr/bin/env python
from collections import deque

from lww.LWWRegister import LWWRegister

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWStack data type.
Based on Specification 9 in https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.
"""      


class LWWStack():
    
    def __init__(self, isFILO = True):
        self.__values = deque()
        self.__isFILO = isFILO
    
    def push(self, value, timestamp):
        self.__values.appendleft(LWWRegister(value, timestamp))
    
    def pop(self) -> LWWRegister:
        return self.__values.popleft() if self.__isFILO else self.__values.pop()
    
    def peek(self):
        return self.__values[0] if self.__isFILO else self.__values[-1]
    
    def getContents(self):
        return self.__values