#!/usr/bin/env python
import uuid
import time

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


class Node(LWWMap):
    
    def __init__(self):
        super().__init__()
        self.__id = uuid.uuid1()
        self._clock = Clock.setUp()
        
    def getId(self):
        return self.__id
    
    def currentTime(self):
        return self._clock.currentTime()
    
    """Naming"""

    def setName(self, name):
        #print("Node: setting name to {}".format(name))
        self._clock.sleepOneStep()
        return self.add(Literals.NAME, name, self.currentTime())
    
    def getName(self):
        #print("Node: returning name {}".format(self.query(Literals.NAME)))
        return self.query(Literals.NAME)
    
    """Typing"""

    def setType(self, node):
        self._clock.sleepOneStep()
        return self.add(Literals.TYPED_BY, node, self.currentTime())
    
    def getType(self):
        return self.query(Literals.TYPED_BY)
        
    """Attributes CRUD"""

    def setAttribute(self, name, value):
        self._clock.sleepOneStep()
        return self.add(name, value, self.currentTime())
    
    def getAttribute(self, name):
        return self.query(name)
    
    def updateAttribute(self, name, value):
        self._clock.sleepOneStep()
        return self.update(name, value, self.currentTime())
    
    def deleteAttribute(self, name):
        self._clock.sleepOneStep()
        self.remove(name, self.currentTime())
