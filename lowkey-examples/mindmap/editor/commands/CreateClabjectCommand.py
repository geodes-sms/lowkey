#!/usr/bin/env python
import logging
import os
import sys

from lowkey.collabtypes.Clabject import Clabject

from .Command import Command

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from metamodel import MindMapPackage

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CreateClabjectCommand(Command):
    
    def __init__(self, tokens):
        self._type = self.findType(tokens[1])
        self._name = tokens[2]
    
    def findType(self, typeString):
        type = next(t for t in MindMapPackage.TYPES.TYPES if t.lower() == typeString.lower())
        if not type:
            raise Exception("Unexpected type {}.".format(typeString))
        return type 
    
    def execute(self, session):
        logging.debug(" Executing command 'CREATE {} {}'.".format(self._type, self._name))
        
        clabject = Clabject()
        clabject.setType(self._type)
        clabject.setName(self._name)
        
        if self._type == MindMapPackage.TYPES.MINDMAP:
            logging.debug("Setting attribute {} with value {}".format(MindMapPackage.TITLE, self._name))
            clabject.setAttribute(MindMapPackage.TITLE, self._name)
        elif self._type == MindMapPackage.TYPES.MARKER:
            logging.debug("Setting attribute {} with value {}".format(MindMapPackage.MARKER_SYMBOL, self._name))
            clabject.setAttribute(MindMapPackage.MARKER_SYMBOL, self._name)
            
        logging.debug(" {} with name {} has been created. Integrating into session {}.".format(clabject.getType(), clabject.getName(), session._id))
        
        session.integrateNode(clabject)
