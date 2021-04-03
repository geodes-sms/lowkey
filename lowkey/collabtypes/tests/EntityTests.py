#!/usr/bin/env python
import unittest

from collabtypes.Entity import Entity

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class Test(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
