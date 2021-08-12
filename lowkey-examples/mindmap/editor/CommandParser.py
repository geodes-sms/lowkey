#!/usr/bin/env python
import logging
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from editor.Command import Command
from editor.CreateAssociationCommand import CreateAssociationCommand
from editor.CreateClabjectCommand import CreateClabjectCommand
from editor.ReadCommand import ReadCommand
from editor.ReadObjectsCommand import ReadObjectsCommand

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CommandParser():
    
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
    
    def parseMessage(self, message) -> Command:
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
    
    def isCreateClabjectCommand(self, tokens):
        return tokens[0].upper() == "CREATE" and len(tokens) == 3
    
    def isLinkCommand(self, tokens):
        return tokens[0].upper() == "LINK" and tokens[2].upper() == "TO" and len(tokens) == 4
    
    def isReadCommand(self, tokens):
        return tokens[0].upper() == "READ" and len(tokens) == 1
    
    def isObjectsCommand(self, tokens):
        return tokens[0].upper() == "OBJECTS" and len(tokens) == 1
    
    def isUpdateCommand(self, tokens):
        return tokens[0].upper() == "UPDATE" and len(tokens) == 4
    
    def isDeleteCommand(self, tokens):
        return tokens[0].upper() == "DELETE" and len(tokens) == 2
