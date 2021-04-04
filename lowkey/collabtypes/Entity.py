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
        self.add(Literals.REALATIONSHIPS, (), self._currentTime())
                
    """Abstract nature"""
    
    def _setAbstract(self, isAbstract:bool):
        return self.add(Literals.IS_ABSTRACT, isAbstract, self._currentTime())
    
    def _isAbstract(self) -> bool:
        return self.query(Literals.IS_ABSTRACT)
    
    """Inheritance"""

    def _extends(self, entity):
        return self.add(Literals.EXTENDS, entity, self._currentTime())
    
    def _super(self):
        return self.query(Literals.EXTENDS)
    
    """Relationships CRUD"""
    
    def _addRelationship(self, relationship:Relationship):
        relationships = self.query(Literals.REALATIONSHIPS)
        relationships = relationships + (relationship,)
        self.update(Literals.REALATIONSHIPS, relationships, self._currentTime())
        
    def _getRelationship(self, name):
        relationships = self.query(Literals.REALATIONSHIPS)
        return [r for r in relationships if r._getAttribute(Literals.NAME) == name]
