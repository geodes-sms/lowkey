#!/usr/bin/env python
import logging

from lowkey.collabapi.commands.Command import Command
from lowkey.collabtypes.Association import Association

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CreateAssociationCommand(Command):
    
    def __init__(self, params):
        self._params = params
    
    def execute(self, session):    
        session.integrateAssociation(self._params)
