#!/usr/bin/env python
import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from editor.Command import Command
from scenarios import PrintHelper2

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class ReadCommand(Command):
    
    def execute(self, session):
        logging.debug(" Executing command 'READ' in session {}.".format(session._id))
        root = session._mindmapmodel
        
        mindmapClabjects = root.getMindmaps()
        
        if mindmapClabjects:
            for mc in mindmapClabjects:
                PrintHelper2.printMindmap(mc)
        else:
            print("No mindmaps defined yet")
