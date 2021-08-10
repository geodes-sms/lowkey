#!/usr/bin/env python
import logging
import uuid

from metamodel.entities.MindMapModel import MindMapModel

from editor import MindMapPackage
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Association import Association
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.MindMap import MindMap
from metamodel.entities.SubTopic import SubTopic

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Session object to manage local modeling data.
"""


class EditorSession():
    
    def __init__(self):
        self._id = uuid.uuid1()
        self._mindmapmodel = MindMapModel()
        self._tmp = []
    
    def classFactory(self, classname):
        if classname.lower() not in [k.lower() for k in globals().keys()]:
            return None
        klass = {k.lower():v for k, v in globals().items()}[classname.lower()]
        return klass()
    
    def integrateNode(self, node):
        node.addToModel(self._mindmapmodel)
            
    def integrateAssociation(self, associationName, fromClabjectName, toClabjectName):
        logging.debug(" Integrating association '{}' between {} and {}.".format(associationName, fromClabjectName, toClabjectName))
        
        fromClabject = self._mindmapmodel.getNodeByName(fromClabjectName)
        toClabject = self._mindmapmodel.getNodeByName(toClabjectName)
        
        association = Association()
        
        association.setName(associationName)
        association.setFrom(fromClabject)
        association.setTo(toClabject)
        
        logging.debug(" Integrating association {} from {} to {}."
                      .format(association.getName(), association.getFrom(), association.getTo()))
        
        self.integrateNode(association)
        
        
