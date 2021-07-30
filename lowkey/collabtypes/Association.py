#!/usr/bin/env python

from lowkey.collabtypes import Literals
from lowkey.lww.LWWMap import LWWMap

from .Node import Node

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Association type for the general logical type model level.
"""


class Association(Node):

    def __init__(self):
        super().__init__()
        self.persistence = LWWMap()
    
    def setFrom(self, clabject):
        self.setFeature(Literals.ASSOCIATION_FROM, clabject)
        
    def getFrom(self):
        return self.getFeature(Literals.ASSOCIATION_FROM)
    
    def setTo(self, clabject):
        self.setFeature(Literals.ASSOCIATION_TO, clabject)
        
    def getTo(self):
        return self.getFeature(Literals.ASSOCIATION_TO)
    
    def setFromMin(self, fromMin):
        self.setFeature(Literals.ASSOCIATION_FROM_MIN, fromMin)
        
    def getFromMin(self):
        return self.getFeature(Literals.ASSOCIATION_FROM_MIN)
    
    def setFromMax(self, fromMax):
        self.setFeature(Literals.ASSOCIATION_FROM_MAX, fromMax)
        
    def getFromMax(self):
        return self.getFeature(Literals.ASSOCIATION_FROM_MAX)
    
    def setToMin(self, toMin):
        self.setFeature(Literals.ASSOCIATION_TO_MIN, toMin)
        
    def getToMin(self):
        return self.getFeature(Literals.ASSOCIATION_TO_MIN)
    
    def setToMax(self, toMax):
        self.setFeature(Literals.ASSOCIATION_TO_MAX, toMax)
        
    def getToMax(self):
        return self.getFeature(Literals.ASSOCIATION_TO_MAX)

    def setComposition(self, isComposition):
        self.setFeature(Literals.ASSOCIATION_IS_COMPOSITION, isComposition)
        
    def isComposition(self):
        return self.getFeature(Literals.ASSOCIATION_IS_COMPOSITION)
    
    def setAggregation(self, isAggregation):
        self.setFeature(Literals.ASSOCIATION_IS_AGGREGATION, isAggregation)
        
    def isAggregation(self):
        return self.getFeature(Literals.ASSOCIATION_IS_AGGREGATION)
