#!/usr/bin/env python

from collabtypes import Literals
from collabtypes.Relationship import Relationship

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
        self.add(Literals.RELATIONSHIPS, (), self.currentTime())
                
    """Abstract nature"""
    
    def setAbstract(self, isAbstract:bool):
        return self.add(Literals.IS_ABSTRACT, isAbstract, self.currentTime())
    
    def isAbstract(self) -> bool:
        return self.query(Literals.IS_ABSTRACT)
    
    """Inheritance"""

    def extends(self, entity):
        return self.add(Literals.EXTENDS, entity, self.currentTime())
    
    def super(self):
        return self.query(Literals.EXTENDS)
    
    """Relationships CRUD"""
    
    def addRelationship(self, relationship:Relationship):
        relationships = self.query(Literals.RELATIONSHIPS)
        relationships = relationships + (relationship,)
        self.update(Literals.RELATIONSHIPS, relationships, self.currentTime())
        
    def getRelationship(self, name):
        relationships = self.query(Literals.RELATIONSHIPS)
        return [r for r in relationships if r.getAttribute(Literals.NAME) == name]
    
    def removeRelationship(self, relationship:Relationship):
        relationships = self.query(Literals.RELATIONSHIPS)
        remainingRelationships = ()
        for r in relationships:
            if r != relationship:
                remainingRelationships = remainingRelationships + (r,)
        
        self.update(Literals.RELATIONSHIPS, remainingRelationships, self.currentTime())
