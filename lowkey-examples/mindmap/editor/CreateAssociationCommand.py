#!/usr/bin/env python
import os
import sys
import logging


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from lowkey.collabtypes.Association import Association
from editor.Command import Command

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CreateAssociationCommand(Command):
    
    def __init__(self, session, tokens):
        self._session = session
        self._name = tokens[2]
        self._sourceName = tokens[3]
        self._targetName = tokens[4]
    
    def execute(self):
        logging.debug(" Executing command 'CREATE ASSOCIATION {} from {} to {}' in session {}."
                      .format(self._name, self._sourceName, self._targetName, self._session._id))
        
        association = Association()
        
        association.setName(self._name)
        association.setFrom(self._sourceName)
        association.setTo(self._targetName)
        
        logging.debug(" Executing command 'CREATE ASSOCIATION {} from {} to {}' in session {}."
                      .format(association.getName(), association.getFrom(), association.getTo(), self._session._id))
        
        self._session.integrateAssociation(association)
