#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Simple memory functionality for the Server component.
"""


class Memory():
    
    def __init__(self):
        self._messages = []
        
    def saveMessage(self, message):
        self._messages.append(message)
        
    def getMessages(self):
        return self._messages
