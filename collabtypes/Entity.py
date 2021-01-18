__author__ = "Istvan David"
__copyright__ = "Copyright 2021"

"""
Entity type for the general logical type model level.
"""

from .Node import Node
from .Relationship import Relationship

class Entity(Node):
    
    def __init__(self, name):
        super().__init__(name)
        self.relationships = []
    
    def addRelationship(self):
        relationship = Relationship('r')
        self.relationships.append(relationship)