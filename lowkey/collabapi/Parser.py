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
    
    __commands = ["CREATE", "LINK", "UPDATE", "DELETE"]
    
    def __init__(self):
        logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)
    
    def __tokenize(self, message):
        return message.split()
    
    def __valid(self, command):
        return command.upper() in self.__commands
    
    def validCommandMessage(self, message):
        tokens = self.__tokenize(message)
        return self.__valid(tokens[0])
    
    def getNodeType(self, message):
        return self.__tokenize(message)[1]
    
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
        if self.validCommandMessage(message):
            logging.debug("Command is valid")
            tokens = self.__tokenize(message)
            if self.isCreateClabjectCommand(tokens):
                return CreateClabjectCommand(self.getParams(message))
            if self.isLinkCommand(tokens):
                return CreateAssociationCommand(self.getParams(message))
        else:
            logging.debug("Command is invalid")
            
    def isCreateClabjectCommand(self, tokens):
        return tokens[0].upper() == "CREATE"
    
    def isLinkCommand(self, tokens):
        return tokens[0].upper() == "LINK"
    
    def isUpdateCommand(self, tokens):
        return tokens[0].upper() == "UPDATE"
    
    def isDeleteCommand(self, tokens):
        return tokens[0].upper() == "DELETE"
