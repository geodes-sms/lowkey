#!/usr/bin/env python
import unittest

from lww.LWWMap import LWWMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWMapTests(unittest.TestCase):

    def testAddEntry(self):
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
        
        
        value3 = "David"
        lwwMap.update(key1, value3, 30)
        
        self.assertEqual(lwwMap.query(key1), value3)
        self.assertEqual(lwwMap.size(), 2)
        
        lwwMap.remove(key1, 30)
        self.assertEqual(lwwMap.query(key1), None)
        self.assertEqual(lwwMap.size(), 1)

if __name__ == "__main__":
    unittest.main()
