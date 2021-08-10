#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Clabject with context.
"""

from .Clabject import Clabject
from .Model import Model


class Entity():

    def __init__(self, clabject: Clabject):
        super().__init__()
        self._clabject = clabject
    
    def getAssociations(self):
        associations = self._clabject.getModel().getAssociations()
        return [a for a in associations if (a.getFrom() == self._clabject or a.getTo() == self._clabject)]
    
    def getAssociationsByName(self, name):
        return [a for a in self.getAssociations() if a.getName() == self._clabject.getName()]
    
    def getOutgoingAssociations(self):
        raise NotImplementedError
    
    def getIncomingAssociations(self):
        raise NotImplementedError
    
    def getContainedNodes(self):
        raise NotImplementedError
