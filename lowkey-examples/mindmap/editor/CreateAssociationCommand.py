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
        self._targetName = tokens[1]
        self._sourceName = tokens[3].split('.')[0]
        self._linkName = tokens[3].split('.')[1]
    
    def execute(self):
        logging.debug(" Executing command 'LINK {} TO {}.{}' in session {}."
                      .format(self._targetName, self._sourceName, self._linkName, self._session._id))
        
        self._session.integrateAssociation(self._linkName, self._sourceName, self._targetName)
