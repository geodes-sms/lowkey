#!/usr/bin/env python
import os
import sys
import threading

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from network.Client import Client

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Example client
"""


class Editor(Client):
    
    __commands = ["CREATE", "READ", "UPDATE", "DELETE"]
    
    def run(self):
        connection_thread = threading.Thread(target=self.subscribe, args=())
        connection_thread.daemon = True
        print("Starting connection thread")
        connection_thread.start()
        print("Starting editor")
        self.editorThread()
        
    def subscriberAction(self):
        msg2 = self._subscriber.recv()
        print("I: received update=%s" % msg2)
    
    def timeoutAction(self):
        pass

    ###################### Editor behavior ######################
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

    def editorThread(self):
        print("Reading user input")
        while True:
            userInput = str(input())
            if not userInput:
                continue
                
            arguments = userInput.split()
            command = arguments[0]
            
            if self.valid(command):
                self._publisher.send(b'CREATE MindMap')
            else:
                print("Invalid command")
                continue


if __name__ == "__main__":
    editor = Editor()
    editor.join()
    editor.run()
