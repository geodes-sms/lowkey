#!/usr/bin/env python
from Publisher import Publisher  # @UnresolvedImport

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Simple editor.
"""


class Editor:
    
    __commands = ['CREATE', 'READ', 'UPDATE', 'DELETE']
    
    def __init__(self):
        self.publisher = Publisher()
        self.readInput()
        
    def valid(self, command):
        return command.upper() in self.__commands
        
    def readInput(self):
        print("Reading user input")
        while True:
            userInput = str(input(">"))
            if not userInput:
                continue
                
            arguments = userInput.split()
            command = arguments[0]
                            
            if not self.valid(command):
                print("Invalid command")
            else:
                self.publisher.sendMessage(userInput)

        
if __name__ == '__main__':
    Editor()
