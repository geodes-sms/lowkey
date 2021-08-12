#!/usr/bin/env python
import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from editor import MindMapPackage
from editor.Command import Command
from lowkey.collabtypes.Clabject import Clabject
from metamodel.entities.MindMap import MindMap, MindMapLiterals
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.SubTopic import SubTopic
from metamodel.entities.Marker import Marker, MarkerLiterals

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CreateClabjectCommand2(Command):
    
    def __init__(self, tokens):
        self._type = self.findType(tokens[1])
        self._name = tokens[2]
    
    def findType(self, typeString):
        type = next(t for t in MindMapPackage.TYPES if t.lower() == typeString.lower())
        if not type:
            raise Exception("Unexpected type {}.".format(typeString))
        return type 
    
    def execute(self, session):
        logging.debug(" Executing command 'CREATE {} {}'.".format(self._type, self._name))
        
        clabject = Clabject()
        clabject.setType(self._type)
        clabject.setName(self._name)
        
        if self._type == MindMapPackage.TYPE_MINDMAP:
            logging.debug("Setting attribute {} with value {}".format(MindMapLiterals.TITLE, self._name))
            clabject.setAttribute(MindMapLiterals.TITLE, self._name)
        elif self._type == MindMapPackage.TYPE_MARKER:
            logging.debug("Setting attribute {} with value {}".format(MarkerLiterals.SYMBOL, self._name))
            clabject.setAttribute(MarkerLiterals.SYMBOL, self._name)
        else:
            logging.error("Unexpected type {}.".format(self._type))
            
        logging.debug(" {} with name {} has been created. Integrating into session {}.".format(clabject.getType(), clabject.getName(), session._id))
        
        session.integrateNode(clabject)
