#!/usr/bin/env python
import logging

from lowkey.collabtypes.Association import Association

from .Command import Command


__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CreateAssociationCommand(Command):
    
    def __init__(self, tokens):
        self._targetName = tokens[1]
        self._sourceName = tokens[3].split('.')[0]
        self._linkName = tokens[3].split('.')[1]
    
    def execute(self, session):
        logging.debug(" Executing command 'LINK {} TO {}.{}' in session {}."
                      .format(self._targetName, self._sourceName, self._linkName, session._id))
        
        session.integrateAssociation(self._linkName, self._sourceName, self._targetName)
