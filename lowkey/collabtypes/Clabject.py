#!/usr/bin/env python
from lowkey.collabtypes import Literals
from lowkey.lww.LWWMap import LWWMap

from .Node import Node


__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Clabject type for the general logical type model level.
"""


class Clabject(Node):
    
    def __init__(self):
        super().__init__()
        self.persistence = LWWMap()
        self.persistence.add(Literals.ASSOCIATIONS, (), self.currentTime())
                
    """Abstract nature"""
    
    def setAbstract(self, isAbstract:bool):
        self.setFeature(Literals.IS_ABSTRACT, isAbstract)
    
    def isAbstract(self) -> bool:
        return self.getFeature(Literals.IS_ABSTRACT)
    
    """Inheritance"""

    def setInheritsFrom(self, clabject):
        assert type(self) is type(clabject)
        self.setFeature(Literals.INHERITS_FROM, clabject)
    
    def getInheritsFrom(self):
        return self.getFeature(Literals.INHERITS_FROM)
    
    """Associations CRUD"""
    '''
    def addAssociation(self, association:Association):
        associations = self.getFeature(Literals.ASSOCIATIONS)
        associations = associations + (association,)
        self.updateFeature(Literals.ASSOCIATIONS, associations)
        
    def getAssociation(self, name):
        associations = self.getFeature(Literals.ASSOCIATIONS)
        return [a for a in associations if a.getFeature(Literals.NAME) == name]
    
    def removeAssociation(self, association:Association):
        associations = self.getFeature(Literals.ASSOCIATIONS)
        remainingAssociations = ()
        for a in associations:
            if a != association:
                remainingAssociations = remainingAssociations + (a,)
        
        self.updateFeature(Literals.ASSOCIATIONS, remainingAssociations)
    '''