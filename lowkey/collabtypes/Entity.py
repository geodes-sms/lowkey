#!/usr/bin/env python

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
        self.__relationships = self._setAttribute("relationships", ())
    
    def _addRelationship(self, relationship:Relationship):
        relationships = self._getAttribute("relationships")
        relationships = relationships + (relationship,)
        self._updateAttribute("relationships", relationships)
        
    def _getRelationship(self, name):
        relationships = self._getAttribute("relationships")
        return [r for r in relationships if r._getAttribute("name") == name]
