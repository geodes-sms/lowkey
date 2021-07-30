#!/usr/bin/env python
import unittest

from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clock import Clock, ClockMode
from lowkey.collabtypes.Entity import Entity

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
        
        association = Association()
        association.setFrom(person)
        association.setTo(university)
        association.setAggregation(False)
        association.setAttribute("name", "affiliation")
        association.setAttribute("directed", "target")
        person.addAssociation(association)
        
        affiliationAssociation = person.getAssociation("affiliation")
        affiliationAssociation = affiliationAssociation[0] if len(affiliationAssociation) == 1 else self.fail()
        
        self.assertEqual(affiliationAssociation.getFrom(), person)
        self.assertEqual(affiliationAssociation.getTo(), university)
        self.assertFalse(affiliationAssociation.isAggregation())
        direction = affiliationAssociation.getAttribute("directed")
        self.assertEqual(direction, "target")


if __name__ == "__main__":
    unittest.main()
