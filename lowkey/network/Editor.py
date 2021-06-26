#!/usr/bin/env python
import os
import sys
import threading
import logging
import argparse

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from network.Client import Client

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Simple command line editor as an example client.
"""


class Editor(Client):
    
    __commands = ["CREATE", "READ", "UPDATE", "DELETE"]
    __encoding = "utf-8"
    
    def run(self):
        connection_thread = threading.Thread(target=self.subscribe, args=())
        connection_thread.daemon = True
        logging.debug("Starting connection thread")
        connection_thread.start()
        logging.debug("Starting editor")
        self.editorThread()
    
    def subscriberAction(self):
        receviedMessage = self._subscriber.recv()
        senderId, message = self.getMessage(receviedMessage)
        
        if self.throwawayMessage(senderId):
            logging.debug("Throwing message {}".format(message))
        else:
            logging.debug("Processing message {}".format(message))
        
    def getMessage(self, rawMessage):
        return rawMessage.decode(self.__encoding).split(' ', 1)        
    
    def throwawayMessage(self, senderId):
        return senderId.replace('[', '').replace(']', '') == str(self._id)
    
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
                msg = self.createMessage(userInput)
                self._publisher.send(msg)
            else:
                print("Invalid command")
                continue

    def createMessage(self, body):
        return bytes('[{}] {}'.format(self._id, body), self.__encoding)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-log",
        "--log",
        default="warning",
        help=("Provide logging level. "
              "Example '--log debug', default='warning'."
              )
        )

    options = parser.parse_args()
    levels = {
        'critical': logging.CRITICAL,
        'error': logging.ERROR,
        'warn': logging.WARNING,
        'warning': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG
    }
    level = levels.get(options.log.lower())
    if level is None:
        raise ValueError(
            f"log level given: {options.log}"
            f" -- must be one of: {' | '.join(levels.keys())}")
    
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=level)
    
    editor = Editor()
    editor.join()
    editor.run()
