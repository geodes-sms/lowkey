#!/usr/bin/env python
import logging
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../lowkey")

from editor.CreateRelationshipCommand import CreateRelationshipCommand
from editor.CreateEntityCommand import CreateEntityCommand
from editor.ReadCommand import ReadCommand

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class CommandParser():
    
    __commands = ["CREATE", "READ", "UPDATE", "DELETE"]
    
    def __init__(self, session):
        self._session = session
    
    def tokenize(self, message):
        return message.split()
    
    def valid(self, command):
        return command.upper() in self.__commands
    
    def validCommandMessage(self, message):
        tokens = self.tokenize(message)
        return tokens[0].upper() in self.__commands
    
    def validCommand(self, tokens):
        return (
            self.isCreateEntityCommand(tokens) or
            self.isCreateRelationshipCommand(tokens) or
            self.isReadCommand(tokens) or
            self.isUpdateCommand(tokens) or
            self.isDeleteCommand(tokens)
        )
    
    def parseMessage(self, message):
        tokens = self.tokenize(message)
        if self.validCommand(tokens):
            logging.debug("Command is valid")
            if self.isReadCommand(tokens):
                return ReadCommand(self._session)
            if self.isCreateEntityCommand(tokens):
                return CreateEntityCommand(self._session, tokens)
            if self.isCreateRelationshipCommand(tokens):
                return CreateRelationshipCommand(self._session, tokens)
        else:
            logging.debug("Command is invalid")
    
    def isCreateEntityCommand(self, tokens):
        return tokens[0].upper() == "CREATE" and len(tokens) == 3
    
    def isCreateRelationshipCommand(self, tokens):
        return tokens[0].upper() == "CREATE" and tokens[1].upper() == "RELATIONSHIP" and len(tokens) == 5
    
    def isReadCommand(self, tokens):
        return tokens[0].upper() == "READ" and len(tokens) == 1
    
    def isUpdateCommand(self, tokens):
        return tokens[0].upper() == "UPDATE" and len(tokens) == 4
    
    def isDeleteCommand(self, tokens):
        return tokens[0].upper() == "DELETE" and len(tokens) == 2
