#!/usr/bin/env python
import time
import uuid

from lww.LWWPlainValueMap import LWWPlainValueMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Abstract Node type for the general logical type model level.

Serves as a common abstraction to the other logical types.
"""


class Node(LWWPlainValueMap):
    
    def __init__(self):
        super().__init__()
        self.__id = uuid.uuid1()
        
    def getId(self):
        return self.__id
        
    # Attribute handling
    def _getAttribute(self, name):
        return self.query(name)
    
    def _setAttribute(self, name, value):
        return self.add(name, value, round(time.time() * 1000))