#!/usr/bin/env python
import unittest

from lowkey.collabapi.Parser import Parser
from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Clock import Clock, ClockMode
from lowkey.collabtypes.Model import Model

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class CollabAPIParserTests(unittest.TestCase):
    
    def setUp(self):
        Clock.setUp(ClockMode.DEBUG)
        
    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
