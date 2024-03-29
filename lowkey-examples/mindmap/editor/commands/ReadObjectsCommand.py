#!/usr/bin/env python
import logging

from lowkey.collabapi.commands.Command import Command

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class ReadObjectsCommand(Command):
    
    def execute(self, session):
        logging.debug(" Executing command 'OBJECTS' in session {}.".format(session._id))
        root = session.getModels()[0]
        
        nodes = root.getNodes()
        
        if nodes:
            for n in nodes:
                print(n.getName(), n)
        else:
            print("No objects in the model yet")
    
