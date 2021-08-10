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
    
    def tearDown(self):
        del(self._model)
    
    def testEntityCreation(self):
        person = Clabject()
        person.addToModel(self._model)
        self.assertEqual(len(self._model.getNodes()), 1)
        self.assertEqual(person.getModel(), self._model)
        
        personEntity = Entity(person)
        self.assertNotEqual(personEntity, None)

    def testEntityQuery(self):
        #type
        person = Clabject()
        self._model.addNode(person)
        self.assertEqual(len(self._model.getNodes()), 1)
        
        #instance
        steve = Clabject()
        steve.setType(person)
        steve.addToModel(self._model)
        self.assertEqual(len(self._model.getNodes()), 2)
        
        #instance
        alice = Clabject()
        alice.setType(person)
        alice.addToModel(self._model)
        self.assertEqual(len(self._model.getNodes()), 3)
        
        queryByTypeResult = self._model.getNodesByType(person)
        self.assertEqual(len(queryByTypeResult), 2)
        self.assertTrue(steve in queryByTypeResult)
        self.assertTrue(alice in queryByTypeResult)
        
        personLink = Association()
        personLink.setFrom(steve)
        personLink.setTo(alice)
        personLink.setName("colleague")
        personLink.addToModel(self._model)
        self.assertEqual(len(self._model.getNodes()), 4)
        self.assertTrue(personLink in self._model.getAssociations())
        
        steveEntity = Entity(steve)
        aliceEntity = Entity(alice)
        
        self.assertEqual(len(steveEntity.getAssociations()), 1)
        self.assertTrue(personLink in steveEntity.getAssociations())

if __name__ == "__main__":
    unittest.main()
