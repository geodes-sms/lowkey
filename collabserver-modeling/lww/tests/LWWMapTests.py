#!/usr/bin/env python
import unittest

from lww.LWWMap import LWWMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWMapTests(unittest.TestCase):

    def testAddAndQueryEntries(self):
        lwwMap = LWWMap()
        
        key1 = "name"
        value1 = "Istvan"
        lwwMap.add(key1, value1, 10)
        
        self.assertEqual(lwwMap.query(key1), value1)
        self.assertEqual(lwwMap.size(), 1)
        
        key2 = "profession"
        value2 = "researcher"
        lwwMap.add(key2, value2, 20)
        
        self.assertEqual(lwwMap.query(key2), value2)
        self.assertEqual(lwwMap.size(), 2)
        
    def testAddAndQueryDuplicateEntry(self):
        lwwMap = LWWMap()
        
        key1 = "name"
        value1 = "Istvan"
        lwwMap.add(key1, value1, 10)
        
        self.assertEqual(lwwMap.query(key1), value1)
        self.assertEqual(lwwMap.size(), 1)
        
        value2 = "David"
        lwwMap.add(key1, value2, 20)
        
        self.assertEqual(lwwMap.size(), 1)
        self.assertEqual(lwwMap.query(key1), value2)
        self.assertNotEqual(lwwMap.query(key1), value1)

        
    def testRemoveAndQueryEntry(self):
        lwwMap = LWWMap()
        
        key1 = "name"
        value1 = "Istvan"
        lwwMap.add(key1, value1, 10)
        
        self.assertEqual(lwwMap.query(key1), value1)
        self.assertEqual(lwwMap.size(), 1)
        
        lwwMap.remove(key1, 30)
        self.assertEqual(lwwMap.size(), 0)

    """
    TODO: assert raises KeyError    
    def testRemoveNotexisting(self):
        lwwMap = LWWMap()
        
        with lwwMap.remove("key", 10):
            self.assertRaises(KeyError)
    """    

if __name__ == "__main__":
    unittest.main()
