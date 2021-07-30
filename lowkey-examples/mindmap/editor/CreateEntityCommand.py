#!/usr/bin/env python
import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from editor import MindMapPackage
from lowkey.collabtypes.Entity import Entity
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.SubTopic import SubTopic
from metamodel.entities.Marker import Marker

from editor.Command import Command

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CreateEntityCommand(Command):
    
    def __init__(self, session, tokens):
        self._session = session
        self._type = tokens[1]
        self._name = tokens[2]
    
    def execute(self):
        logging.debug(" Executing command 'CREATE {} {}'.".format(self._type, self._name))
        
        entity = None
        
        if self._type.lower() == MindMapPackage.TYPE_CENTRAL_TOPIC.lower():
            logging.debug("Instantiating {} with name {}".format(MindMapPackage.TYPE_CENTRAL_TOPIC, self._name))
            entity = CentralTopic()
            entity.setName(self._name)
            entity.setType(MindMapPackage.TYPE_CENTRAL_TOPIC)
        elif self._type.lower() == MindMapPackage.TYPE_MAIN_TOPIC.lower():
            logging.debug("Instantiating {} with name {}".format(MindMapPackage.TYPE_MAIN_TOPIC, self._name))
            entity = MainTopic()
            entity.setName(self._name)
            entity.setType(MindMapPackage.TYPE_MAIN_TOPIC)
        elif self._type.lower() == MindMapPackage.TYPE_SUBTOPIC.lower():
            logging.debug("Instantiating {} with name {}".format(MindMapPackage.TYPE_SUBTOPIC, self._name))
            entity = SubTopic()
            entity.setName(self._name)
            entity.setType(MindMapPackage.TYPE_SUBTOPIC)
        elif self._type.lower() == MindMapPackage.TYPE_MARKER.lower():
            logging.debug("Instantiating {} with name {}".format(MindMapPackage.TYPE_MARKER, self._name))
            entity = Marker()
            entity.setName(self._name)
            entity.setType(MindMapPackage.TYPE_MARKER)
        else:
            logging.error("Unexpected type {}.".format(self._type))
            
        logging.debug(entity)

        logging.debug(" {} with name {} has been created. Integrating into session {}.".format(entity.getType(), entity.getName(), self._session._id))
        
        self._session.integrateEntity(entity)
