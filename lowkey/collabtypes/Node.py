#!/usr/bin/env python
import time
import uuid

from lowkey.collabtypes import Literals
from lowkey.collabtypes.Clock import Clock
from lowkey.lww.LWWMap import LWWMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Abstract Node type for the general logical type model level.

Serves as a common abstraction to the other logical types.
"""


class Node():
    
    def __init__(self):
        super().__init__()
        self.__id = uuid.uuid1()
        self._clock = Clock.setUp()
        
    def getId(self):
        return self.__id
    
    def currentTime(self):
        return self._clock.currentTime()
    
    """CRDT persistence"""

    def getPersistence(self):
        return self.persistence
    
    """Naming"""

    def setName(self, name):
        return self.setFeature(Literals.NAME, name)
    
    def getName(self):
        return self.getFeature(Literals.NAME)
    
    """Typing"""

    def setType(self, node):
        return self.setFeature(Literals.TYPED_BY, node)
    
    def getType(self):
        return self.getFeature(Literals.TYPED_BY)
        
    """Attributes CRUD"""

    def setAttribute(self, name, value):
        return self.setFeature(name, value)
    
    def getAttribute(self, name):
        return self.getFeature(name)
    
    def updateAttribute(self, name, value):
        return self.updateFeature(name, value)
    
    def deleteAttribute(self, name):
        self.deleteFeature(name)

    """Features CRUD"""

    def setFeature(self, name, value):
        self._clock.sleepOneStep()
        return self.persistence.add(name, value, self.currentTime())
    
    def getFeature(self, name):
        return self.persistence.query(name)
    
    def updateFeature(self, name, value):
        self._clock.sleepOneStep()
        return self.persistence.update(name, value, self.currentTime())
    
    def deleteFeature(self, name):
        self._clock.sleepOneStep()
        self.persistence.remove(name, self.currentTime())
