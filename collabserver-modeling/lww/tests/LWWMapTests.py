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
        
        key = "ABC"
        value = 123
        lwwMap.add(key, value, 10)
        
        self.assertEqual(lwwMap.query(key), value)
        
        lwwMap.remove(key, 20)
        self.assertEqual(lwwMap.query(key), None)
        

if __name__ == "__main__":
    unittest.main()
