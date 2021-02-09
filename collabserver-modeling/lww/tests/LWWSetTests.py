#!/usr/bin/env python
import unittest

from lww import Time
from lww.LWWSet import LWWSet


__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWSetTests(unittest.TestCase):
       
    def testSimpleAdd(self):
        lwwSet = LWWSet()
        
        key = "someKey"
        self.assertFalse(lwwSet.query(key))
        
        lwwSet.add(key, Time.current())
        self.assertTrue(lwwSet.query(key))
        
    def testSimpleRemove(self):
        lwwSet = LWWSet()
        
        key = "someKey"
        self.assertFalse(lwwSet.query(key))
        
        lwwSet.add(key, Time.current())
        self.assertTrue(lwwSet.query(key))
        
        lwwSet.remove(key, Time.current())
        self.assertFalse(lwwSet.query(key))
        
    def testSize(self):
        lwwSet = LWWSet()
        self.assertEqual(lwwSet.size(), 0)
        
        lwwSet.add("element1", Time.current())
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add("element1", Time.current())
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add("element2", Time.current())
        self.assertEqual(lwwSet.size(), 2)
        
        lwwSet.remove("element1", Time.current())
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.remove("element1", Time.current())
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.remove("element3", Time.current())
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.remove("element2", Time.current())
        self.assertEqual(lwwSet.size(), 0)
     
    def testClear(self):
        lwwSet = LWWSet()
        self.assertEqual(lwwSet.size(), 0)
        
        lwwSet.add("element1", Time.current())
        self.assertEqual(lwwSet.size(), 1)
        
        lwwSet.add("element2", Time.current())
        self.assertEqual(lwwSet.size(), 2)
        
        lwwSet.clear(Time.current())
        self.assertEqual(lwwSet.size(), 0)

if __name__ == "__main__":
    unittest.main()
