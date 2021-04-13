#!/usr/bin/env python

from collabtypes import Literals

from .Node import Node

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Relationship type for the general logical type model level.
"""


class Relationship(Node):

    def __init__(self):
        super().__init__()
    
    def setFrom(self, entity):
        self.setAttribute(Literals.RELATIONSHIP_FROM, entity)
        
    def getFrom(self):
        return self.getAttribute(Literals.RELATIONSHIP_FROM)
    
    def setTo(self, entity):
        self.setAttribute(Literals.RELATIONSHIP_TO, entity)
        
    def getTo(self):
        return self.getAttribute(Literals.RELATIONSHIP_TO)
    
    def setAggregation(self, isAggregation):
        self.setAttribute(Literals.RELATIONSHIP_ISAGGREGATION, isAggregation)
        
    def isAggregation(self):
        return self.getAttribute(Literals.RELATIONSHIP_ISAGGREGATION)
