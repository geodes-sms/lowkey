#!/usr/bin/env python
import os
import sys
import logging


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from lowkey.collabtypes.Relationship import Relationship
from editor.Command import Command

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CreateRelationshipCommand(Command):
    
    def __init__(self, session, tokens):
        self._session = session
        self._name = tokens[2]
        self._sourceName = tokens[3]
        self._targetName = tokens[4]
    
    def execute(self):
        logging.debug(" Executing command 'CREATE RELATIONSHIP {} from {} to {}' in session {}."
                      .format(self._name, self._sourceName, self._targetName, self._session._id))
        
        relationship = Relationship()
        
        relationship.setName(self._name)
        relationship.setFrom(self._sourceName)
        relationship.setTo(self._targetName)
        
        logging.debug(" Executing command 'CREATE RELATIONSHIP {} from {} to {}' in session {}."
                      .format(relationship.getName(), relationship.getFrom(), relationship.getTo(), self._session._id))
        
        self._session.integrateRelationship(relationship)
