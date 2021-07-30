#!/usr/bin/env python
import argparse
import logging
import os
import sys
import threading

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from editor.CommandParser import CommandParser
from editor.EditorSession import EditorSession
from lowkey.network.Client import Client

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
        
        self._session = EditorSession()
        
        self.parser = CommandParser(self._session)
    
    def run(self):
        connection_thread = threading.Thread(target=self.subscribe, args=())
        connection_thread.daemon = True
        logging.debug("Starting connection thread")
        connection_thread.start()
        logging.debug("Starting editor")
        self.editorThread()
    
    def join(self):
        self._snapshot.send(b"request_snapshot")
        while True:
            try:
                receviedMessage = self._snapshot.recv()
                logging.debug("Received message {}".format(receviedMessage))
                _, message = self.getMessage(receviedMessage)
                self.consumeMessage(message)
            except:
                return  # Interrupted
            if message == b"finished_snapshot":
                # sequence = kvmsg.sequence
                logging.debug("Received snapshot")
                break  # Done
    
    def subscriberAction(self):
        receviedMessage = self._subscriber.recv()
        senderId, message = self.getMessage(receviedMessage)
        
        if self.throwawayMessage(senderId):
            logging.debug("Throwing message {}".format(message))
        else:
            logging.debug("Processing message {}".format(message))
            self.consumeMessage(message)
    
    def getMessage(self, rawMessage):
        return rawMessage.decode(self.__encoding).split(' ', 1)
    
    def consumeMessage(self, message):
        command = self.parser.parseMessage(message)
        command.execute()
    
    def throwawayMessage(self, senderId):
        return senderId.replace('[', '').replace(']', '') == str(self._id)
    
    def timeoutAction(self):
        pass

    ###################### Editor behavior ######################
    
    def editorThread(self):
        print("Reading user input")
        while True:
            userInput = str(input())
            if not userInput:
                continue
            
            if self.parser.validCommandMessage(userInput):
                self.consumeMessage(userInput)  # Process in current session
                if(self.parser.tokenize(userInput)[0].upper() != "READ"):
                    message = self.createMessage(userInput)
                    self._publisher.send(message)  # Publish to other client sessions
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
