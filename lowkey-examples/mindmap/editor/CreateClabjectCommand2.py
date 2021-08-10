#!/usr/bin/env python
import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from editor import MindMapPackage
from lowkey.collabtypes.Clabject import Clabject
from metamodel.entities.MindMap import MindMap, MindMapLiterals
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.SubTopic import SubTopic
from metamodel.entities.Marker import Marker, MarkerLiterals

from editor.Command import Command

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CreateClabjectCommand2(Command):
    
    def __init__(self, session, tokens):
        self._session = session
        self._type = self.findType(tokens[1])
        self._name = tokens[2]
    
    def findType(self, typeString):
        type = next(t for t in MindMapPackage.TYPES if t.lower() == typeString.lower())
        if not type:
            raise Exception("Unexpected type {}.".format(typeString))
        return type 
    
    def execute(self):
        logging.debug(" Executing command 'CREATE {} {}'.".format(self._type, self._name))
        
        logmessage = "Instantiating {} with name {}"
        
        clabject = Clabject()
        clabject.setType(self._type)
        clabject.setName(self._name)
        
        if self._type == MindMapPackage.TYPE_MINDMAP:
            logging.debug(logmessage.format(MindMapPackage.TYPE_MINDMAP, self._name))
            clabject.setAttribute(MindMapLiterals.TITLE, self._name)
        elif self._type.lower() == MindMapPackage.TYPE_MARKER.lower():
            logging.debug(logmessage.format(MindMapPackage.TYPE_MARKER, self._name))
            clabject.setAttribute(MarkerLiterals.SYMBOL, self._name)
        else:
            logging.error("Unexpected type {}.".format(self._type))
            
        logging.debug(clabject)

        logging.debug(" {} with name {} has been created. Integrating into session {}.".format(clabject.getType(), clabject.getName(), self._session._id))
        
        self._session.integrateNode(clabject)
