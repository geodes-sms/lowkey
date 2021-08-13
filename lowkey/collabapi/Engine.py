#!/usr/bin/env python
import uuid

from lowkey.collabapi.Parser import Parser
from lowkey.collabapi.Session import Session


__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
TODO: Add description
"""


class Engine():
    
    def __init__(self):
        self._id = uuid.uuid1()
        self._session = Session()
        self._parser = Parser()
        
    def getSession(self):
        return self._session
    
    def getParser(self):
        return self._parser
    
