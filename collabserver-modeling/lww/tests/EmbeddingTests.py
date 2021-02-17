#!/usr/bin/env python
import unittest

from lww.LWWRegister import LWWRegister
from lww.LWWSet import LWWSet

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class EmbeddingTests(unittest.TestCase):

    def testEmbedRegisterInRegister(self):
        base = LWWRegister()
        embedded = LWWRegister()
        
        value = "hello"
        
        embedded.update(value, 10)
        base.update(embedded, 20)
        
        retrievedEmbedded = base.query()    
        self.assertTrue(retrievedEmbedded)
        self.assertTrue(isinstance(retrievedEmbedded, LWWRegister))
        
        self.assertTrue(retrievedEmbedded.query())
        self.assertEqual(retrievedEmbedded.query(), value)
        self.assertTrue(isinstance(retrievedEmbedded.query(), str))
        
    def testEmbedSetInRegister(self):
        base = LWWRegister()
        embedded = LWWSet()
                
        value = "element1"
        
        embedded.add(value, 10)
        base.update(embedded, 20)
        
        retrievedEmbedded = base.query()
        self.assertTrue(retrievedEmbedded)
        self.assertTrue(isinstance(retrievedEmbedded, LWWSet))        
        self.assertTrue(retrievedEmbedded.query(value))
        
    def testEmbedRegisterInSet(self):
        base = LWWSet()
        embedded = LWWRegister()
                
        value = "element1"
        
        embedded.update(value, 10)
        base.add(embedded, 20)
        
        self.assertTrue(base.query(embedded))
        
    def testEmbedSetInSet(self):
        base = LWWSet()
        embedded = LWWSet()
                
        value = "element1"
        
        embedded.add(value, 10)
        base.add(embedded, 20)
        
        self.assertTrue(base.query(embedded))
        
        newValue = "element2"
        embedded.add(newValue, 30)
        
        self.assertTrue(base.query(embedded))
        self.assertTrue(embedded.query(value))
        self.assertTrue(embedded.query(newValue))


if __name__ == "__main__":
    unittest.main()
