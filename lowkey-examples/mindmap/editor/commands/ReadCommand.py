#!/usr/bin/env python
import logging
import os
import sys

from .Command import Command

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from facilities import PrintHelper

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class ReadCommand(Command):
    
    def execute(self, session):
        logging.debug(" Executing command 'READ' in session {}.".format(session._id))
        root = session.getModels()[0]
        
        mindmapClabjects = root.getMindmaps()
        
        if mindmapClabjects:
            for mc in mindmapClabjects:
                PrintHelper.printMindmap(mc)
        else:
            print("No mindmaps defined yet")
