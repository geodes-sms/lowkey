#!/usr/bin/env python
import logging
import uuid

from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clabject import Clabject

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
TODO: Add description
"""


class Session():
    
    def __init__(self):
        self._id = uuid.uuid1()
        self._models = []
    
    def addModel(self, model):
        self._models.append(model)
        
    def getModels(self):
        return self._models
    
    def getModelById(self, id):
        return next(m for m in self.getModels() if m.getId() == id)
    
    def integrateNode(self, node):
        node.addToModel(self.getModels()[0])
            
    def integrateAssociation(self, associationName, fromClabjectName, toClabjectName):
        logging.debug(" Integrating association '{}' between {} and {}.".format(associationName, fromClabjectName, toClabjectName))
        
        fromClabject = self.getModels()[0].getNodeByName(fromClabjectName)
        toClabject = self.getModels()[0].getNodeByName(toClabjectName)
        
        association = Association()
        
        association.setName(associationName)
        association.setFrom(fromClabject)
        association.setTo(toClabject)
        
        logging.debug(" Integrating association {} from {} to {}."
                      .format(association.getName(), association.getFrom(), association.getTo()))
        
        self.integrateNode(association)
        
