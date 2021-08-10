#!/usr/bin/env python
import unittest

from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clock import Clock, ClockMode
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Model import Model

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class ClabjectTests(unittest.TestCase):

    def testClabjectCreation(self):
        Clock.setUp(ClockMode.DEBUG)
        
        model = Model()
        
        person = Clabject()
        model.addNode(person)
        self.assertEqual(len(model.getNodes()), 1)
        
        personAsClabject = model.getClabjects()[0]
        self.assertEqual(personAsClabject, person)
        
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
        
        attributeName3 = "name"
        attributeValue3 = "University of Montreal"
        university = Clabject()
        university.setAttribute(attributeName3, attributeValue3)
        
        returnValue3 = university.getAttribute(attributeName3)
        self.assertEqual(returnValue3, attributeValue3)
        
        association = Association()
        association.setFrom(person)
        association.setTo(university)
        association.setAggregation(False)
        association.setAttribute("name", "affiliation")
        association.setAttribute("directed", "target")
        model.addNode(association)
        self.assertEqual(len(model.getNodes()), 2)
        
        affiliationLinkAsNode = model.getNodeByName("affiliation")
        self.assertEqual(affiliationLinkAsNode.getFrom(), person)
        
        affiliationLinkAsAssociation = model.getAssociations()[0]
        self.assertEqual(affiliationLinkAsAssociation.getFrom(), person)
        
        affiliationAssociation = affiliationLinkAsAssociation
        
        self.assertEqual(affiliationAssociation.getFrom(), person)
        self.assertEqual(affiliationAssociation.getTo(), university)
        self.assertFalse(affiliationAssociation.isAggregation())
        direction = affiliationAssociation.getAttribute("directed")
        self.assertEqual(direction, "target")
        
        man = Clabject()
        person.setInheritsFrom(man)
        self.assertEqual(person.getInheritsFrom(), man)
        
        employment = Association()
        association.setInheritsFrom(employment)
        self.assertEqual(association.getInheritsFrom(), employment)
        
        with self.assertRaises(AssertionError):
            association.setInheritsFrom(man)
        self.assertEqual(association.getInheritsFrom(), employment)
    
    def testNodeCannotBeAddedToModelTwice(self):
        Clock.setUp(ClockMode.DEBUG)
        
        model = Model()
        
        person = Clabject()
        model.addNode(person)
        self.assertEqual(len(model.getNodes()), 1)
        
        with self.assertRaises(Exception):
            person.addToModel(model)
        self.assertEqual(len(model.getNodes()), 1)
        
    def testQueryByStringType(self):
        Clock.setUp(ClockMode.DEBUG)
        
        model = Model()
        
        personType = "PERSON"
        
        person = Clabject()
        person.setType(personType)
        model.addNode(person)
        
        self.assertEqual(len(model.getNodes()), 1)
        self.assertEqual(model.getNodes()[0], person)
        
        queryByTypeResult = model.getNodeByType(personType)
        self.assertEqual(queryByTypeResult, person)
        
    def testQueryByNodeType(self):
        Clock.setUp(ClockMode.DEBUG)
        
        model = Model()
        
        #type
        person = Clabject()
        model.addNode(person)
        self.assertEqual(len(model.getNodes()), 1)
        
        #instance
        steve = Clabject()
        steve.setType(person)
        model.addNode(steve)
        self.assertEqual(len(model.getNodes()), 2)
        
        queryByTypeResult = model.getNodeByType(person)
        self.assertEqual(queryByTypeResult, steve)


if __name__ == "__main__":
    unittest.main()
