#!/usr/bin/env python
from Publisher import Publisher

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Simple editor.
"""


class Editor:
    
    __commands = ["CREATE", "READ", "UPDATE", "DELETE"]
    
    def __init__(self):
        self.publisher = Publisher()
        self.readInput()
        
    def valid(self, command):
        return command.upper() in self.__commands
    
    def isCreateEntityCommand(self, arguments):
        return arguments[0].upper() == "CREATE" and len(arguments) == 3
    
    def isCreateRelationshipCommand(self, arguments):
        return arguments[0].upper() == "CREATE" and arguments[0].upper() == "association" and len(arguments) == 5
    
    def isReadCommand(self, arguments):
        return arguments[0].upper() == "READ" and len(arguments) == 1
    
    def isUpdateCommand(self, arguments):
        return arguments[0].upper() == "UPDATE" and len(arguments) == 4
    
    def isDeleteCommand(self, arguments):
        return arguments[0].upper() == "DELETE" and len(arguments) == 2
        
    def readInput(self):
        print("Reading user input")
        while True:
            userInput = str(input(">"))
            if not userInput:
                continue
                
            arguments = userInput.split()
            command = arguments[0]
            
            if self.valid(command):
                self.publisher.sendMessage(userInput)
            else:
                print("Invalid command")
                continue

        
if __name__ == "__main__":
    Editor()
