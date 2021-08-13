#!/usr/bin/env python
import unittest

from lowkey.collabapi.Parser import Parser
from lowkey.collabapi.Session import Session
from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Clock import Clock, ClockMode
from lowkey.collabtypes.Model import Model

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class SessionTests(unittest.TestCase):
    
    def setUp(self):
        Clock.setUp(ClockMode.DEBUG)
        self._session = Session()
        
    def tearDown(self):
        del(self._session)

    def testAddModel(self):
        model = Model()
        self._session.addModel(model)
        
        self.assertEqual(len(self._session.getModels()), 1)
        
    def testGetModelFromSessionById(self):
        model = Model()
        self._session.addModel(model)
        
        self.assertEqual(len(self._session.getModels()), 1)
        
        id = model.getId()
        
        self.assertEqual(self._session.getModelById(id), model)


if __name__ == "__main__":
    unittest.main()
