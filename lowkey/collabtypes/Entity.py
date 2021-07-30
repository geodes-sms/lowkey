#!/usr/bin/env python

from lowkey.collabtypes import Literals
from lowkey.collabtypes.Relationship import Relationship
from lowkey.lww.LWWMap import LWWMap

from .Node import Node

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Entity type for the general logical type model level.
"""


class Entity(Node):
    
    def __init__(self):
        super().__init__()
        self.persistence = LWWMap()
        self.persistence.add(Literals.RELATIONSHIPS, (), self.currentTime())
                
    """Abstract nature"""
    
    def setAbstract(self, isAbstract:bool):
        self._clock.sleepOneStep()
        return self.persistence.add(Literals.IS_ABSTRACT, isAbstract, self.currentTime())
    
    def isAbstract(self) -> bool:
        return self.persistence.query(Literals.IS_ABSTRACT)
    
    """Inheritance"""

    def extends(self, entity):
        self._clock.sleepOneStep()
        return self.persistence.add(Literals.EXTENDS, entity, self.currentTime())
    
    def super(self):
        return self.persistence.query(Literals.EXTENDS)
    
    """Relationships CRUD"""
    
    def addRelationship(self, relationship:Relationship):
        self._clock.sleepOneStep()
        relationships = self.persistence.query(Literals.RELATIONSHIPS)
        relationships = relationships + (relationship,)
        self.persistence.update(Literals.RELATIONSHIPS, relationships, self.currentTime())
        
    def getRelationship(self, name):
        relationships = self.persistence.query(Literals.RELATIONSHIPS)
        return [r for r in relationships if r.getAttribute(Literals.NAME) == name]
    
    def removeRelationship(self, relationship:Relationship):
        self._clock.sleepOneStep()
        relationships = self.query(Literals.RELATIONSHIPS)
        remainingRelationships = ()
        for r in relationships:
            if r != relationship:
                remainingRelationships = remainingRelationships + (r,)
        
        self.persistence.update(Literals.RELATIONSHIPS, remainingRelationships, self.currentTime())
