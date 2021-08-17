#!/usr/bin/env python
import unittest

from lowkey.collabapi.Parser import Parser
from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Clock import Clock, ClockMode
from lowkey.collabtypes.Model import Model
from lowkey.collabtypes import Literals

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class CollabAPIParserTests(unittest.TestCase):
    
    def setUp(self):
        Clock.setUp(ClockMode.DEBUG)
        self._parser = Parser()
        
    def tearDown(self):
        del(self._parser)
    
    def testCommandValidity(self):
        messages = ["CREATE Clabject", "UPDATE Clabject", "DELETE Clabject"]
        for message in messages:
            tokens = self._parser.tokenize(message)
            self.assertTrue(self._parser.validCommand(tokens[0].upper()))
            
        message = "CREAT Clabject"
        tokens = self._parser.tokenize(message)
        self.assertFalse(self._parser.validCommand(tokens[0].upper()))
        
    def testParams(self):
        param1Name = "name"
        param1Value = "mm1"
        param2Name = "type"
        param2Value = "mindmap"
        
        message = "CREATE Clabject -{} {} -{} {}".format(param1Name, param1Value, param2Name, param2Value)
        parameters = self._parser.getParams(message)
            
        name1, value1 = parameters[0]
        self.assertEqual(name1, param1Name)
        self.assertEqual(value1, param1Value)
        
        name2, value2 = parameters[1]
        self.assertEqual(name2, param2Name)
        self.assertEqual(value2, param2Value)


if __name__ == "__main__":
    unittest.main()
