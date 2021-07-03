#!/usr/bin/env python
import copy
import unittest

from lowkey.lww.LWWMap import LWWMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class CloningTests(unittest.TestCase):
    
    lwwMap = None
    
    def setUp(self):
        self.lwwMap = LWWMap()
        
    def tearDown(self):
        self.lwwMap = None

    def testImproperCloneHasDifferentId(self):
        clone = LWWMap()
        self.assertNotEqual(self.lwwMap.getId(), clone.getId())
        
    def testProperCloneHasIdenticalId(self):
        clone = copy.deepcopy(self.lwwMap)
        self.assertEqual(self.lwwMap.getId(), clone.getId())
        
if __name__ == "__main__":
    unittest.main()
