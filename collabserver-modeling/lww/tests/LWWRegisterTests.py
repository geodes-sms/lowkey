#!/usr/bin/env python
import unittest

from lww.LWWRegister import LWWRegister

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWRegisterTests(unittest.TestCase):
    
    def testLWWRegisterEquality(self):
        r1 = LWWRegister()
        r1.update("hello", 10)

        r2 = LWWRegister()
        r2.update("world", 20)

        r3 = LWWRegister(prototype=r1)
        r3.update("yo", 30)

        self.assertTrue(r1 != r2)
        self.assertTrue(r1 == r3)
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1, r3)
    
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
        
    def testIdGeneration(self):
        lwwRegister1 = LWWRegister()
        self.assertTrue(lwwRegister1.getId())
        lwwRegister2 = LWWRegister()
        self.assertTrue(lwwRegister2.getId())
        self.assertNotEqual(lwwRegister1.getId(), lwwRegister2.getId())
        
    def testSameIdForPrototypes(self):
        lwwRegister1 = LWWRegister()
        self.assertTrue(lwwRegister1.getId())
        lwwRegister2 = LWWRegister(prototype=lwwRegister1)
        self.assertTrue(lwwRegister2.getId())
        self.assertEqual(lwwRegister1.getId(), lwwRegister2.getId())

if __name__ == "__main__":
    unittest.main()
