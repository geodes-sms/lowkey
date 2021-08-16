#!/usr/bin/env python
import logging
import os
import sys

from lowkey.collabapi.commands.CreateClabjectCommand import CreateClabjectCommand

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from editor.commands.ReadCommand import ReadCommand
from editor.commands.ReadObjectsCommand import ReadObjectsCommand

from metamodel import MindMapPackage

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class DSLParser():
    
    __commands = ["CREATE", "READ", "OBJECTS", "LINK", "UPDATE", "DELETE"]
    
    def tokenize(self, message):
        return message.split()
    
    def valid(self, command):
        return command.upper() in self.__commands
    
    def validCommandMessage(self, message):
        tokens = self.tokenize(message)
        return tokens[0].upper() in self.__commands
    
    def validCommand(self, tokens):
        return (
            self.isCreateClabjectCommand(tokens) or
            self.isLinkCommand(tokens) or
            self.isReadCommand(tokens) or
            self.isUpdateCommand(tokens) or
            self.isObjectsCommand(tokens) or
            self.isDeleteCommand(tokens)
        )
    
    def parseMessage(self, message):
        tokens = self.tokenize(message)
        if self.validCommand(tokens):
            logging.debug("Command is valid")
            if self.isReadCommand(tokens):
                return ReadCommand()
            if self.isObjectsCommand(tokens):
                return ReadObjectsCommand()
            if self.isCreateClabjectCommand(tokens):
                return CreateClabjectCommand(tokens)
            if self.isLinkCommand(tokens):
                return CreateAssociationCommand(tokens)
        else:
            logging.debug("Command is invalid")
    
    def translateMessageIntoCollabAPICommand(self, message):
        tokens = self.tokenize(message)
        
        command = ''
        
        if tokens[0].upper() == 'CREATE':
            userCommand, type, name = tokens 
            command += '{} -typedBy {} -name {}'.format(userCommand, type, name)
            
            if type == MindMapPackage.TYPES.MINDMAP:
                command += ' -title {}'.format(name)
            elif type == MindMapPackage.TYPES.MARKER:
                command += ' -symbol {}'.format(name)
        elif tokens[0].upper() == 'LINK':
            userCommand, sourceAndPort, _toKeyWord, target = tokens
            source, name = sourceAndPort.split('.') 
            command += '{} -from {} -to {} -name {}'.format(userCommand, source, target, name)
        
        return command
    
    def isCreateClabjectCommand(self, tokens):
        return tokens[0].upper() == "CREATE"
    
    def isLinkCommand(self, tokens):
        return tokens[0].upper() == "LINK"
    
    def isReadCommand(self, tokens):
        return tokens[0].upper() == "READ" and len(tokens) == 1
    
    def isObjectsCommand(self, tokens):
        return tokens[0].upper() == "OBJECTS" and len(tokens) == 1
    
    def isUpdateCommand(self, tokens):
        return tokens[0].upper() == "UPDATE"
    
    def isDeleteCommand(self, tokens):
        return tokens[0].upper() == "DELETE"
