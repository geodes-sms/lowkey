#!/usr/bin/env python
import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from editor.Command import Command

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CreateEntityCommand(Command):
    
    def __init__(self, session, tokens):
        self._session = session
        self._type = tokens[1]
        self._name = tokens[2]
    
    def execute(self):
        logging.debug(" Executing command 'CREATE {} {}' in session {}.".format(self._type, self._name, self._session._id))
        self._session.createEntity(self._type, self._name)
