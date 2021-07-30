#!/usr/bin/env python

from lowkey.collabtypes import Literals
from lowkey.lww.LWWMap import LWWMap

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
        self.persistence = LWWMap()
    
    def setFrom(self, entity):
        self.setFeature(Literals.RELATIONSHIP_FROM, entity)
        
    def getFrom(self):
        return self.getFeature(Literals.RELATIONSHIP_FROM)
    
    def setTo(self, entity):
        self.setFeature(Literals.RELATIONSHIP_TO, entity)
        
    def getTo(self):
        return self.getFeature(Literals.RELATIONSHIP_TO)
    
    def setFromMin(self, fromMin):
        self.setFeature(Literals.RELATIONSHIP_FROM_MIN, fromMin)
        
    def getFromMin(self):
        return self.getFeature(Literals.RELATIONSHIP_FROM_MIN)
    
    def setFromMax(self, fromMax):
        self.setFeature(Literals.RELATIONSHIP_FROM_MAX, fromMax)
        
    def getFromMax(self):
        return self.getFeature(Literals.RELATIONSHIP_FROM_MAX)
    
    def setToMin(self, toMin):
        self.setFeature(Literals.RELATIONSHIP_TO_MIN, toMin)
        
    def getToMin(self):
        return self.getFeature(Literals.RELATIONSHIP_TO_MIN)
    
    def setToMax(self, toMax):
        self.setFeature(Literals.RELATIONSHIP_TO_MAX, toMax)
        
    def getToMax(self):
        return self.getFeature(Literals.RELATIONSHIP_TO_MAX)

    def setComposition(self, isComposition):
        self.setFeature(Literals.RELATIONSHIP_IS_COMPOSITION, isComposition)
        
    def isComposition(self):
        return self.getFeature(Literals.RELATIONSHIP_IS_COMPOSITION)
    
    def setAggregation(self, isAggregation):
        self.setFeature(Literals.RELATIONSHIP_IS_AGGREGATION, isAggregation)
        
    def isAggregation(self):
        return self.getFeature(Literals.RELATIONSHIP_IS_AGGREGATION)
