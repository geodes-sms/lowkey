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
        self.setFeature(Literals.IS_ABSTRACT, isAbstract)
    
    def isAbstract(self) -> bool:
        return self.getFeature(Literals.IS_ABSTRACT)
    
    """Inheritance"""

    def setInheritsFrom(self, entity):
        self.setFeature(Literals.INHERITS_FROM, entity)
    
    def getInheritsFrom(self):
        return self.getFeature(Literals.INHERITS_FROM)
    
    """Relationships CRUD"""
    
    def addRelationship(self, relationship:Relationship):
        relationships = self.getFeature(Literals.RELATIONSHIPS)
        relationships = relationships + (relationship,)
        self.updateFeature(Literals.RELATIONSHIPS, relationships)
        
    def getRelationship(self, name):
        relationships = self.getFeature(Literals.RELATIONSHIPS)
        return [r for r in relationships if r.getFeature(Literals.NAME) == name]
    
    def removeRelationship(self, relationship:Relationship):
        relationships = self.getFeature(Literals.RELATIONSHIPS)
        remainingRelationships = ()
        for r in relationships:
            if r != relationship:
                remainingRelationships = remainingRelationships + (r,)
        
        self.updateFeature(Literals.RELATIONSHIPS, remainingRelationships)
