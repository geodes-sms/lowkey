#!/usr/bin/env python
import unittest

from lww.LWWMap import LWWMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWMapTests(unittest.TestCase):
    
    lwwMap = None
    
    def setUp(self):
        self.lwwMap = LWWMap()
        
    def tearDown(self):
        self.lwwMap = None

    def testAddAndQueryEntries(self):
        key1 = "name"
        value1 = "Istvan"
        self.lwwMap.add(key1, value1, 10)
        
        self.assertTrue(self.lwwMap.lookup(key1))
        
        self.assertEqual(self.lwwMap.query(key1), value1)
        self.assertEqual(self.lwwMap.size(), 1)
        
        key2 = "profession"
        value2 = "researcher"
        self.lwwMap.add(key2, value2, 20)
        
        self.assertEqual(self.lwwMap.query(key2), value2)
        self.assertEqual(self.lwwMap.size(), 2)
    
    def testAddingWithExistingKeyIsProcessedButNotExistsImmediately(self):
        key1 = "name"
        value1 = "Istvan"
        self.lwwMap.add(key1, value1, 10)
        
        self.assertEqual(self.lwwMap.query(key1), value1)
        self.assertEqual(self.lwwMap.size(), 1)
        
        value2 = "David"
        self.lwwMap.add(key1, value2, 20)
        self.assertEqual(self.lwwMap.query(key1), value2)
        self.assertEqual(self.lwwMap.size(), 1)
        
    def testRemoveAndQueryEntry(self):
        key1 = "name"
        value1 = "Istvan"
        self.lwwMap.add(key1, value1, 10)
        
        self.assertEqual(self.lwwMap.query(key1), value1)
        self.assertEqual(self.lwwMap.size(), 1)
        
        self.lwwMap.remove(key1, 30)
        self.assertFalse(self.lwwMap.lookup(key1), value1)
        self.assertEqual(self.lwwMap.size(), 0)

    def testIterateOverEntries(self):
        key1 = "firstName"
        value1 = "Istvan"
        self.lwwMap.add(key1, value1, 10)
        key2 = "lastName"
        value2 = "David"
        self.lwwMap.add(key2, value2, 20)
        
        self.assertEqual(self.lwwMap.query(key1), value1)
        self.assertEqual(self.lwwMap.query(key2), value2)
        self.assertEqual(self.lwwMap.size(), 2)
        
        entrySet = self.lwwMap.entrySet()
        
        entriesVisited = 0
        for (key, value), _ in entrySet:
            if(key == key1):
                self.assertEqual(value, value1)
                entriesVisited += 1
            elif(key == key2):
                self.assertEqual(value, value2)
                entriesVisited += 1
            else:
                self.fail()
                
        self.assertEqual(entriesVisited, 2)
                
        key3 = "profession"
        value3 = "researcher"
        self.lwwMap.add(key3, value3, 30)
        
        entriesVisited = 0
        for (key, value), _ in entrySet:
            if(key == key1):
                self.assertEqual(value, value1)
                entriesVisited += 1
            elif(key == key2):
                self.assertEqual(value, value2)
                entriesVisited += 1
            elif(key == key3):
                self.assertEqual(value, value3)
                entriesVisited += 1
            else:
                self.fail()
                
        self.assertEqual(entriesVisited, 3)
        
    def testIterateOverKeys(self):
        key1 = "firstName"
        value1 = "Istvan"
        self.lwwMap.add(key1, value1, 10)
        key2 = "lastName"
        value2 = "David"
        self.lwwMap.add(key2, value2, 20)
        
        self.assertEqual(self.lwwMap.query(key1), value1)
        self.assertEqual(self.lwwMap.query(key2), value2)
        self.assertEqual(self.lwwMap.size(), 2)
        
        keySet = self.lwwMap.keySet()
        
        entriesVisited = 0
        for key in keySet:
            if(key == key1):
                self.assertEqual(self.lwwMap.query(key), value1)
                entriesVisited += 1
            elif(key == key2):
                self.assertEqual(self.lwwMap.query(key), value2)
                entriesVisited += 1
            else:
                self.fail()
                
        self.assertEqual(entriesVisited, 2)

    """
    def testRemoveNotexisting(self):
        lwwMap = LWWMap()
        
        self.assertRaises(KeyError, lwwMap.remove, "key", 10)
    """


if __name__ == "__main__":
    unittest.main()
