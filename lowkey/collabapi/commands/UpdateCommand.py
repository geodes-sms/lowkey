#!/usr/bin/env python
import logging

from lowkey.collabapi.commands.Command import Command
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes import Literals

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class UpdateCommand(Command):
    
    def __init__(self, params):
        self._params = params
    
    def execute(self, session):
        clabject = None
        
        x = [p for p in self._params if p[0] == Literals.ID]
        if x:
            logging.debug("Finding clabject by ID.")
            idParam = x[0]
            clabjectId = idParam[1]
            clabject = session.getModels()[0].getNodeById(clabjectId)
        else:
            logging.debug("Finding clabject by name.")
            nameParam = next(p for p in self._params if p[0] == Literals.NAME)
            clabjectName = nameParam[1]
            clabject = session.getModels()[0].getNodeByName(clabjectName)
                
        for param in [p for p in self._params if p[0] != Literals.NAME]:
            name = param[0]
            value = param[1]
            logging.debug("Executing command 'clabject.updateFeature({}, {})'.".format(name, value))
            clabject.updateFeature(name, value)
