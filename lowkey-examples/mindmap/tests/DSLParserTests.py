#!/usr/bin/env python
import logging
import os
import sys
import unittest

from mindmap.editor.DSLParser import DSLParser
from mindmap.editor.MindmapSession import MindmapSession

from lowkey.collabapi.Parser import Parser
from lowkey.collabtypes.Clock import Clock, ClockMode
from metamodel import MindMapPackage
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.Marker import Marker
from metamodel.entities.MindMap import MindMap
from metamodel.entities.MindMapModel import MindMapModel


__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class DSLParserTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(DSLParserTests, cls).setUpClass()
        logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.ERROR)
    
    def setUp(self):
        Clock.setUp(ClockMode.DEBUG)
        self._dslParser = DSLParser()
        self._collabParser = Parser()
        
    def tearDown(self):
        del(self._dslParser)
        del(self._collabParser)
        
    def testCommandTranslation(self):
        message = "CREATE mindmap mm1"
        
        collabCommand = self._dslParser.translateMessageIntoCollabAPICommand(message)
        
        # print(collabCommand)
        
        self.assertTrue(self._collabParser.validCommandMessage(collabCommand))


if __name__ == "__main__":
    unittest.main()
