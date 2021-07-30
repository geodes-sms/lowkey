#!/usr/bin/env python
import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from editor import MindMapPackage
from lowkey.collabtypes.Clabject import Clabject
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


class CreateClabjectCommand(Command):
    
    def __init__(self, session, tokens):
        self._session = session
        self._type = tokens[1]
        self._name = tokens[2]
    
    def execute(self):
        logging.debug(" Executing command 'CREATE {} {}'.".format(self._type, self._name))
        
        clabject = None
        
        if self._type.lower() == MindMapPackage.TYPE_CENTRAL_TOPIC.lower():
            logging.debug("Instantiating {} with name {}".format(MindMapPackage.TYPE_CENTRAL_TOPIC, self._name))
            clabject = CentralTopic()
            clabject.setName(self._name)
            clabject.setType(MindMapPackage.TYPE_CENTRAL_TOPIC)
        elif self._type.lower() == MindMapPackage.TYPE_MAIN_TOPIC.lower():
            logging.debug("Instantiating {} with name {}".format(MindMapPackage.TYPE_MAIN_TOPIC, self._name))
            clabject = MainTopic()
            clabject.setName(self._name)
            clabject.setType(MindMapPackage.TYPE_MAIN_TOPIC)
        elif self._type.lower() == MindMapPackage.TYPE_SUBTOPIC.lower():
            logging.debug("Instantiating {} with name {}".format(MindMapPackage.TYPE_SUBTOPIC, self._name))
            clabject = SubTopic()
            clabject.setName(self._name)
            clabject.setType(MindMapPackage.TYPE_SUBTOPIC)
        elif self._type.lower() == MindMapPackage.TYPE_MARKER.lower():
            logging.debug("Instantiating {} with name {}".format(MindMapPackage.TYPE_MARKER, self._name))
            clabject = Marker()
            clabject.setName(self._name)
            clabject.setType(MindMapPackage.TYPE_MARKER)
        else:
            logging.error("Unexpected type {}.".format(self._type))
            
        logging.debug(clabject)

        logging.debug(" {} with name {} has been created. Integrating into session {}.".format(clabject.getType(), clabject.getName(), self._session._id))
        
        self._session.integrateClabject(clabject)
