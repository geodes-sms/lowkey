#!/usr/bin/env python
import unittest

from lowkey.lww.LWWSet import LWWSet

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWSetTests(unittest.TestCase):

    def testExistsOnEmptySetReturnsFalse(self):
        lwwSet = LWWSet()
        self.assertFalse(lwwSet.lookup("element"))

    def testAddingElementMakesItExist(self):
        lwwSet = LWWSet()
        
        key = "element"
        self.assertFalse(lwwSet.lookup(key))
        
        lwwSet.add(key, 10)
        self.assertTrue(lwwSet.lookup(key))
        
    def testAddingOlderValuesIsOmitted(self):
        lwwSet = LWWSet()
        
        key = "element"
        self.assertEqual(lwwSet.size(), 0)
        
        addTime1 = 20
        addTime2 = 10
        
        lwwSet.add(key, addTime1)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add(key, addTime2)
        self.assertEqual(lwwSet.size(), 1)
    
    def testAddingElementsReflectsInSize(self):
        lwwSet = LWWSet()
        
        element1 = "element1"
        element2 = "element2"
        
        self.assertEqual(lwwSet.size(), 0)
        
        lwwSet.add(element1, 10)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add(element2, 20)
        self.assertEqual(lwwSet.size(), 2)
        
    def testRemovingElementsReflectsInSize(self):
        lwwSet = LWWSet()
        
        element1 = "element1"
        element2 = "element2"
        
        self.assertEqual(lwwSet.size(), 0)
        
        lwwSet.add(element1, 10)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add(element2, 20)
        self.assertEqual(lwwSet.size(), 2)
        
        lwwSet.remove(element2, 30)
        self.assertEqual(lwwSet.size(), 1)

    def testAddingDuplicatesIsOmitted(self):
        lwwSet = LWWSet()
        
        key1 = "element1"
        key2 = "element2"
        self.assertEqual(lwwSet.size(), 0)
        
        lwwSet.add(key1, 10)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add(key2, 20)
        self.assertEqual(lwwSet.size(), 2)
        
        lwwSet.add(key1, 30)
        self.assertEqual(lwwSet.size(), 2)

    def testRemovedElementDoesNotExist(self):
        lwwSet = LWWSet()
        
        key = "element"
        self.assertFalse(lwwSet.lookup(key))
        
        addTime = 10
        removeTime = 20
        
        lwwSet.add(key, addTime)
        self.assertTrue(lwwSet.lookup(key))
        
        lwwSet.remove(key, removeTime)
        self.assertFalse(lwwSet.lookup(key))
        
    def testAddRemoveAdd(self):
        lwwSet = LWWSet()
        self.assertEqual(lwwSet.size(), 0)
        
        element1 = "element1"
        
        lwwSet.add(element1, 10)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.remove(element1, 20)
        self.assertEqual(lwwSet.size(), 0)
        
        lwwSet.add(element1, 30)
        self.assertEqual(lwwSet.size(), 1)
        
    def testAddAddRemoveWithDelay(self):
        lwwSet = LWWSet()
        self.assertEqual(lwwSet.size(), 0)
        
        element1 = "element1"
        
        lwwSet.add(element1, 10)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add(element1, 30)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.remove(element1, 20)
        self.assertEqual(lwwSet.size(), 1)
    
    def testSize(self):
        lwwSet = LWWSet()
        self.assertEqual(lwwSet.size(), 0)
        
        element1 = "element1"
        element2 = "element2"
        element3 = "element3"
        
        lwwSet.add(element1, 10)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add(element1, 15)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add(element2, 20)
        self.assertEqual(lwwSet.size(), 2)
        
        lwwSet.remove(element1, 25)
        self.assertFalse(lwwSet.lookup(element1))
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.remove(element1, 30)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.remove(element3, 35)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add(element3, 40)
        self.assertEqual(lwwSet.size(), 2)
        
        lwwSet.remove(element2, 45)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.remove(element3, 50)
        self.assertEqual(lwwSet.size(), 0)
    
    def testClear(self):
        lwwSet = LWWSet()
        self.assertEqual(lwwSet.size(), 0)
        
        lwwSet.add("element1", 10)
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add("element2", 20)
        self.assertEqual(lwwSet.size(), 2)
        
        lwwSet.clear(30)
        self.assertEqual(lwwSet.size(), 0)

    def testIterations(self):
        lwwSet = LWWSet()
        
        lwwSet.add("element1", 10)    
        lwwSet.add("element2", 20)
        self.assertEqual(lwwSet.size(), 2)
        
        i = 0
        for _ in lwwSet:
            i += 1
        self.assertEqual(i, 2)
        
        lwwSet.add("element3", 30)
        self.assertEqual(lwwSet.size(), 3)
        
        i = 0
        for _ in lwwSet:
            i += 1
        self.assertEqual(i, 3)
        
        lwwSet.remove("element2", 40)
        self.assertEqual(lwwSet.size(), 2)
        
        i = 0
        for _ in lwwSet:
            i += 1
        self.assertEqual(i, 2)
        
        lwwSet.add("element3", 50)
        self.assertEqual(lwwSet.size(), 2)
        
        i = 0
        for _ in lwwSet:
            i += 1
        self.assertEqual(i, 2)
        
        lwwSet.clear(60)
        self.assertEqual(lwwSet.size(), 0)
        
        i = 0
        for _ in lwwSet:
            i += 1
        self.assertEqual(i, 0)  
    
    def testIterationContents(self):
        lwwSet = LWWSet()
        
        elements = ["element1", "element2"]
        
        lwwSet.add(elements[0], 10)    
        lwwSet.add(elements[1], 20)
        self.assertEqual(lwwSet.size(), 2)
        
        for value, _ in lwwSet:
            self.assertTrue(value in elements)


if __name__ == "__main__":
    unittest.main()
