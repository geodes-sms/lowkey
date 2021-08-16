#!/usr/bin/env python
import os
import sys
import unittest
import logging

from mindmap.editor.DSLParser import DSLParser
from mindmap.editor.MindmapSession import MindmapSession

from lowkey.collabapi.Parser import Parser
from lowkey.collabtypes.Clock import Clock, ClockMode
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.Marker import Marker
from metamodel.entities.MindMap import MindMap
from metamodel.entities.MindMapModel import MindMapModel
from metamodel import MindMapPackage

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class NetworkStub():
    
    def __init__(self, localSession, remoteSession):
        self._localSession = localSession
        self._remoteSession = remoteSession
    
    def forward(self, message):
        # self._collabParser.parseMessage(message, self._remoteSession)
        self._remoteSession.processMessage(message)


if __name__ == "__main__":
    unittest.main()
