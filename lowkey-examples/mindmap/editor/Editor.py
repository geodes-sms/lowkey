#!/usr/bin/env python
import argparse
import logging
import os
import sys
import threading

from DSLParser import DSLParser
from MindmapSession import MindmapSession
from lowkey.network.Client import Client

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from metamodel.entities.MindMapModel import MindMapModel

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Simple command line editor as an example client.
"""


class Editor(Client):
    __encoding = "utf-8"
    
    def __init__(self):
        super().__init__()
        self._session = MindmapSession()
        self._parser = DSLParser()
    
    def run(self):
        connection_thread = threading.Thread(target=self.subscribe, args=())
        connection_thread.daemon = True
        logging.debug("Starting connection thread")
        connection_thread.start()
        logging.debug("Starting editor")
        self.editorThread()
    
    # Join a server and receive the updates
    def join(self):
        self._snapshot.send(b"request_snapshot")
        while True:
            try:
                receviedMessage = self._snapshot.recv()
                logging.debug("Received message {}".format(receviedMessage))
                _, message = self.getMessage(receviedMessage)
                self.processMessage(message)
            except:
                return  # Interrupted
            if message == b"finished_snapshot":
                logging.debug("Received snapshot")
                break  # Done
    
    # The behavior that will be executed in the polling loop
    def subscriberAction(self):
        receviedMessage = self._subscriber.recv()
        senderId, message = self.getMessage(receviedMessage)
        
        if self.throwawayMessage(senderId):
            logging.debug("Throwing message {}".format(message))
        else:
            logging.debug("Processing message {}".format(message))
            self.processMessage(message)
    
    # Editor thread for interacting with the local user
    def editorThread(self):
        print("Reading user input")
        while True:
            userInput = str(input())
            if not userInput:
                continue
            
            tokens = self._parser.tokenize(userInput)
            commandKeyWord = tokens[0].upper()
            if self._parser.isLocalCommand(commandKeyWord):
                commandObject = self._parser.processLocalMessage(commandKeyWord)
                commandObject.execute(self._session)
            elif self._parser.isGlobalCommand(commandKeyWord):
                collabAPICommand = self._parser.translateIntoCollabAPICommand(userInput)
                # process locally
                self._session.processMessage(collabAPICommand)
                # produce remote message and publish
                body = collabAPICommand
                message = self.createMessage(body)
                self._publisher.send(message)
            else:
                print("Invalid command")
                continue
    
    '''
    Message production
    '''
    
    def messageToBeForwarded(self, command):
        return command in ["READ", "OBJECTS"]
    
    def createMessage(self, body):
        return bytes('[{}] {}'.format(self._id, body), self.__encoding)
    
    '''
    Message processing
    '''

    def getMessage(self, rawMessage):
        return rawMessage.decode(self.__encoding).split(' ', 1)
        
    def throwawayMessage(self, senderId):
        return senderId.replace('[', '').replace(']', '') == str(self._id)

    def processMessage(self, message):
        self._session.processMessage(message)
    
    '''
    Timeout action
    '''

    def timeoutAction(self):
        pass


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
