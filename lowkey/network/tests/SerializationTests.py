#!/usr/bin/env python
import unittest
import json
from types import SimpleNamespace

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class Dummy():
    
    def __init__(self):
        self.name:str = "Dummy object"
        self.id:int = 1234


class SerializationTests(unittest.TestCase):

    def testDump(self):
        dummy = Dummy()
        jsondata = json.dumps(dummy.__dict__)
        dummy2 = json.loads(jsondata, object_hook=lambda d: SimpleNamespace(**d))
        self.assertEqual(dummy.name, dummy2.name)
        self.assertEqual(dummy.id, dummy2.id)


if __name__ == "__main__":
    unittest.main()
