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
        
    def testIterateOverEntries(self):
        lwwMap = LWWMap()
        
        key1 = "firstName"
        value1 = "Istvan"
        lwwMap.add(key1, value1, 10)
        key2 = "lastName"
        value2 = "David"
        lwwMap.add(key2, value2, 20)
        
        self.assertEqual(lwwMap.query(key1), value1)
        self.assertEqual(lwwMap.query(key2), value2)
        self.assertEqual(lwwMap.size(), 2)
        
        entrySet = lwwMap.entrySet()
        
        entriesVisited = 0
        for key, value in entrySet:
            if(key==key1):
                self.assertEqual(value, value1)
                entriesVisited+=1
            elif(key==key2):
                self.assertEqual(value, value2)
                entriesVisited+=1
            else:
                self.fail()
                
        self.assertEqual(entriesVisited, 2)
                
        key3 = "profession"
        value3 = "researcher"
        lwwMap.add(key3, value3, 30)
        
        entriesVisited = 0
        for key, value in entrySet:
            if(key==key1):
                self.assertEqual(value, value1)
                entriesVisited+=1
            elif(key==key2):
                self.assertEqual(value, value2)
                entriesVisited+=1
            elif(key==key3):
                self.assertEqual(value, value3)
                entriesVisited+=1
            else:
                self.fail()
                
        self.assertEqual(entriesVisited, 3)

    """
    TODO: assert raises KeyError    
    def testRemoveNotexisting(self):
        lwwMap = LWWMap()
        
        with lwwMap.remove("key", 10):
            self.assertRaises(KeyError)
    """    

if __name__ == "__main__":
    unittest.main()
