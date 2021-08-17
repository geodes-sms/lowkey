#!/usr/bin/env python
import re
import logging

from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes import Literals

from lowkey.collabapi.commands.CreateClabjectCommand import CreateClabjectCommand
from lowkey.collabapi.commands.CreateAssociationCommand import CreateAssociationCommand

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Parser for the Collab API.


CREATE -name {name} -typedBy {type} [-params VALUES...]*

clabject = Clabject()
clabject.setFeature(Literals.NAME, {name})
clabject.setFeature(Literals.TYPED_BY, {type})

LINK -from {fromClabject}.{associationName} -to {toClabject} [-params VALUES...]*
association = Association()
association.setFeature(Literals.NAME, name)
association.setFeature(Literals.ASSOCIATION_FROM, {fromClabject})
association.setFeature(Literals.ASSOCIATION_TO, {toClabject})

"""


class Parser():
    
    _commands = ["CREATE", "LINK", "UPDATE", "DELETE"]
    
    def __init__(self):
        logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)
    
    def tokenize(self, message):
        return message.split()
    
    def validCommand(self, command):
        return command in self._commands
    
    def getParams(self, message):
        pattern = "[\-][a-zA-Z0-9]*\s[a-zA-Z0-9]*"
        
        parameters = []
        
        rawParameters = re.findall(pattern, message)
        for p in rawParameters:
            name, value = p.split()
            name = re.sub("\-", "", name)
            parameters.append([name, value])
        
        return parameters
    
    def parseMessage(self, message):
        tokens = self.tokenize(message)
        commandKeyWord = tokens[0].upper()
        
        if commandKeyWord == "CREATE":
            return CreateClabjectCommand(self.getParams(message))
        elif commandKeyWord == "LINK":
            return CreateAssociationCommand(self.getParams(message))
        else:
            logging.debug("Command is unsupported or invalid")
