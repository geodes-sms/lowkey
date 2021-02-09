#!/usr/bin/env python
import unittest

from lww.LWWRegister import LWWRegister

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWRegisterTests(unittest.TestCase):
    
    def testSimpleUpdate(self):
        lwwRegister = LWWRegister()
        lwwRegister.update("message 1", 10)
        self.assertEqual(lwwRegister.query(), "message 1")
        
    def testMultipleUpdates(self):
        lwwRegister = LWWRegister()
        lwwRegister.update("message 1", 10)
        self.assertEqual(lwwRegister.query(), "message 1")
        lwwRegister.update("message 2", 11)
        self.assertEqual(lwwRegister.query(), "message 2")
        
    def testUpdateWithMultipleTypes(self):
        lwwRegister = LWWRegister()
        lwwRegister.update("message 1", 10)
        self.assertEqual(lwwRegister.query(), "message 1")
        lwwRegister.update(1234, 11)
        self.assertEqual(lwwRegister.query(), 1234)


if __name__ == "__main__":
    unittest.main()