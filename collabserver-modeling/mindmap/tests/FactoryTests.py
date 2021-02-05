#!/usr/bin/env python
import unittest
from mindmap.metamodel.entities.Marker import Marker


__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

class Test(unittest.TestCase):
    
    def testFactory(self):
        klass = globals()["Marker"]
        instance = klass()
        print(instance)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFactory']
    unittest.main()