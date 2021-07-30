#!/usr/bin/env python
import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from editor.Command import Command
from scenarios import PrintHelper

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class ReadCommand(Command):
    
    def __init__(self, session):
        self._session = session
    
    def execute(self):
        logging.debug(" Executing command 'READ' in session {}.".format(self._session._id))
        root = self._session._mindmap
        
        #print("Root: {}".format(root))
        # ct = root.getTopic()
        # print("Central topic: {}".format(ct.getName()))
        
        PrintHelper.printMindmap(root)
