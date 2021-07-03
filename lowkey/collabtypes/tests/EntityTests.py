#!/usr/bin/env python
import unittest

from lowkey.collabtypes.Entity import Entity
from lowkey.collabtypes.Relationship import Relationship

from lowkey.collabtypes.Clock import Clock, ClockMode

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class EntityTests(unittest.TestCase):

    def testEntityCreation(self):
        Clock.setUp(ClockMode.DEBUG)
        
        person = Entity()
        
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
        university = Entity()
        university.setAttribute(attributeName3, attributeValue3)
        
        returnValue3 = university.getAttribute(attributeName3)
        self.assertEqual(returnValue3, attributeValue3)
        
        relationship = Relationship()
        relationship.setFrom(person)
        relationship.setTo(university)
        relationship.setAggregation(False)
        relationship.setAttribute("name", "affiliation")
        relationship.setAttribute("directed", "target")
        person.addRelationship(relationship)
        
        affiliationRelationship = person.getRelationship("affiliation")
        affiliationRelationship = affiliationRelationship[0] if len(affiliationRelationship) == 1 else self.fail()
        
        self.assertEqual(affiliationRelationship.getFrom(), person)
        self.assertEqual(affiliationRelationship.getTo(), university)
        self.assertFalse(affiliationRelationship.isAggregation())
        direction = affiliationRelationship.getAttribute("directed")
        self.assertEqual(direction, "target")


if __name__ == "__main__":
    unittest.main()
