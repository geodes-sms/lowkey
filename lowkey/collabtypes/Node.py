#!/usr/bin/env python
import time
import uuid

from collabtypes import Literals

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
    
    def currentTime(self):
        return round(time.time() * 1000)
    
    """Naming"""

    def setName(self, name):
        return self.add(Literals.NAME, name, self.currentTime())
    
    def getName(self):
        return self.query(Literals.NAME)
    
    """Typing"""

    def setType(self, node):
        return self.add(Literals.TYPED_BY, node, self.currentTime())
    
    def getType(self):
        return self.query(Literals.TYPED_BY)
        
    """Attributes CRUD"""

    def setAttribute(self, name, value):
        return self.add(name, value, self.currentTime())
    
    def getAttribute(self, name):
        return self.query(name)
    
    def updateAttribute(self, name, value):
        return self.update(name, value, self.currentTime())
    
    def deleteAttribute(self, name):
        self.remove(name, self.currentTime())
