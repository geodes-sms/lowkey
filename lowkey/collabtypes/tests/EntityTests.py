#!/usr/bin/env python
import time
import unittest

from collabtypes.Entity import Entity
from collabtypes.Relationship import Relationship

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


def halt():
    time.sleep(0.001)


class EntityTests(unittest.TestCase):

    def testEntityCreation(self):
        person = Entity()
        
        attributeName1 = "name"
        attributeValue1 = "Istvan"
        person._setAttribute(attributeName1, attributeValue1)
        halt()
        
        attributeName2 = "profession"
        attributeValue2 = "Researcher"
        person._setAttribute(attributeName2, attributeValue2)
        halt()
        
        returnValue1 = person._getAttribute(attributeName1)
        returnValue2 = person._getAttribute(attributeName2)
        
        self.assertEqual(returnValue1, attributeValue1)
        self.assertEqual(returnValue2, attributeValue2)
        
        attributeName3 = "name"
        attributeValue3 = "University of Montreal"
        university = Entity()
        university._setAttribute(attributeName3, attributeValue3)
        halt()
        
        returnValue3 = university._getAttribute(attributeName3)
        self.assertEqual(returnValue3, attributeValue3)
        
        relationship = Relationship()
        relationship.setFrom(person)
        halt()
        relationship.setTo(university)
        halt()
        relationship.setAggregation(False)
        halt()
        relationship._setAttribute("name", "affiliation")
        halt()
        relationship._setAttribute("directed", "target")
        halt()
        person._addRelationship(relationship)
        halt()
        
        affiliationRelationship = person._getRelationship("affiliation")
        affiliationRelationship = affiliationRelationship[0] if len(affiliationRelationship) == 1 else self.fail()
        
        self.assertEqual(affiliationRelationship.getFrom(), person)
        self.assertEqual(affiliationRelationship.getTo(), university)
        self.assertFalse(affiliationRelationship.isAggregation())
        direction = affiliationRelationship._getAttribute("directed")
        self.assertEqual(direction, "target")


if __name__ == "__main__":
    unittest.main()
