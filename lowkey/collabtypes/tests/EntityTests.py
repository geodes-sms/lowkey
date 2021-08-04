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

    def testEntityCreation(self):
        Clock.setUp(ClockMode.DEBUG)
        
        model = Model()
        
        person = Entity()
        person.setModel(model)
        self.assertEqual(len(model.getNodes()), 1)
        self.assertEqual(person.getModel(), model)
        
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
