#!/usr/bin/env python
import logging

from lowkey.collabapi.commands.Command import Command
from lowkey.collabtypes.Clabject import Clabject

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CreateClabjectCommand(Command):
    
    def __init__(self, params):
        self._params = params
    
    def execute(self, session):
        clabject = Clabject()
        
        for param in self._params:
            name = param[0]
            value = param[1]
            logging.debug("Executing command 'clabject.setFeature({}, {})'.".format(name, value))
            clabject.setFeature(name, value)
            
        session.integrateNode(clabject)
