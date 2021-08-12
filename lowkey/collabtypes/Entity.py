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
        
    def update(self):
        raise NotImplementedError
    
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
    
    """ From Clabject """

    def setAbstract(self, isAbstract:bool):
        self._clabject.setAbstract(isAbstract)
    
    def isAbstract(self) -> bool:
        return self._clabject.isAbstract()

    def setInheritsFrom(self, clabject):
        self._clabject.setInheritsFrom(clabject)
    
    def getInheritsFrom(self):
        return self._clabject.getInheritsFrom()
    
    """ From Node """

    def getId(self):
        return self._clabject.getId()
    
    def currentTime(self):
        return self._clabject.currentTime()

    def getPersistence(self):
        return self._clabject.getPersistence()

    def setName(self, name):
        return self._clabject.setName(name)
    
    def getName(self):
        return self._clabject.getName()
    
    def setType(self, type):
        return self._clabject.setType(type)
    
    def getType(self):
        return self._clabject.getType()
    
    def addToModel(self, model):
        self._clabject.addToModel(model)
    
    def getModel(self):
        return self._clabject.getModel()
        
    def changeModel(self, oldModel, newModel):
        self._clabject.changeModel(oldModel, newModel)
        
    def removeFromModel(self, model):
        self._clabject.removeFromModel(model)

    def setAttribute(self, name, value):
        return self._clabject.setAttribute(name, value)
    
    def getAttribute(self, name):
        return self._clabject.getAttribute(name)
    
    def updateAttribute(self, name, value):
        return self._clabject.updateAttribute(name, value)
    
    def deleteAttribute(self, name):
        self._clabject.deleteAttribute(name)

    def setFeature(self, name, value):
        return self._clabject.setFeature(name, value)
    
    def getFeature(self, name):
        return self._clabject.getFeature(name)
    
    def updateFeature(self, name, value):
        return self._clabject.updateFeature(name, value)
    
    def deleteFeature(self, name):
        self._clabject.deleteFeature(name)
