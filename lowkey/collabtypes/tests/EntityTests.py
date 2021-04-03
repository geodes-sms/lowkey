#!/usr/bin/env python
import unittest

from collabtypes.Entity import Entity
from collabtypes.Relationship import Relationship

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class EntityTests(unittest.TestCase):

    def testEntityCreation(self):
        entity = Entity()
        
        attributeName1 = "name"
        attributeValue1 = "Istvan"
        entity._setAttribute(attributeName1, attributeValue1)
        
        attributeName2 = "profession"
        attributeValue2 = "Researcher"
        entity._setAttribute(attributeName2, attributeValue2)
        
        returnValue1 = entity._getAttribute(attributeName1)
        returnValue2 = entity._getAttribute(attributeName2)
        
        self.assertEqual(returnValue1, attributeValue1)
        self.assertEqual(returnValue2, attributeValue2)
        
        relationship = Relationship()
        relationship._setAttribute("name", "affiliation")
        relationship._setAttribute("directed", "target")
        
        entity2 = Entity()
        entity2._setAttribute("name", "University of Montreal")
        
        entity._addRelationship(relationship)
        
        returnedRelationship = entity._getRelationship("affiliation")
        self.assertEqual(len(returnedRelationship), 1,)
        direction = returnedRelationship[0]._getAttribute("directed")
        
        self.assertEqual(direction, "target")


if __name__ == "__main__":
    unittest.main()
