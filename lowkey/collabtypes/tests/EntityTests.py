#!/usr/bin/env python
import unittest

from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clock import Clock, ClockMode
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Entity import Entity
from lowkey.collabtypes.Model import Model

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class EntityTests(unittest.TestCase):
    
    def setUp(self):
        Clock.setUp(ClockMode.DEBUG)
        self._model = Model()
    
    def testEntityCreation(self):
        person = Entity()
        person.addToModel(self._model)
        self.assertEqual(len(self._model.getNodes()), 1)
        self.assertEqual(person.getModel(), self._model)

    def testEntityCreationViaConstructor(self):
        person = Entity(self._model)
        self.assertEqual(len(self._model.getNodes()), 1)
        self.assertEqual(person.getModel(), self._model)

    def testFullEntity(self):
        person = Entity()
        person.addToModel(self._model)
        self.assertEqual(len(self._model.getNodes()), 1)
        self.assertEqual(person.getModel(), self._model)
        
        attributeName1 = "name"
        attributeValue1 = "Istvan"
        person.setAttribute(attributeName1, attributeValue1)
        
        attributeName2 = "profession"
        attributeValue2 = "Researcher"
        person.setAttribute(attributeName2, attributeValue2)
        
        returnValue1 = person.getAttribute(attributeName1)
        returnValue2 = person.getAttribute(attributeName2)
        
        self.assertEqual(returnValue1, attributeValue1)
        self.assertEqual(returnValue2, attributeValue2)
        
        

if __name__ == "__main__":
    unittest.main()
