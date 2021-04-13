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
    
    def setFromMin(self, fromMin):
        self.setAttribute(Literals.RELATIONSHIP_FROM_MIN, fromMin)
        
    def getFromMin(self):
        return self.getAttribute(Literals.RELATIONSHIP_FROM_MIN)
    
    def setFromMax(self, fromMax):
        self.setAttribute(Literals.RELATIONSHIP_FROM_MAX, fromMax)
        
    def getFromMax(self):
        return self.getAttribute(Literals.RELATIONSHIP_FROM_MAX)
    
    def setToMin(self, toMin):
        self.setAttribute(Literals.RELATIONSHIP_TO_MIN, toMin)
        
    def getToMin(self):
        return self.getAttribute(Literals.RELATIONSHIP_TO_MIN)
    
    def setToMax(self, toMax):
        self.setAttribute(Literals.RELATIONSHIP_TO_MAX, toMax)
        
    def getToMax(self):
        return self.getAttribute(Literals.RELATIONSHIP_TO_MAX)
    
    def setAggregation(self, isAggregation):
        self.setAttribute(Literals.RELATIONSHIP_ISAGGREGATION, isAggregation)
        
    def isAggregation(self):
        return self.getAttribute(Literals.RELATIONSHIP_ISAGGREGATION)
