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
        self.__name:str = "Dummy object"
        self.__id:int = 1234


class SerializationTest(unittest.TestCase):

    def testDump(self):
        dummy = Dummy()
        print(dummy)
        jsondata = json.dumps(dummy.__dict__)
        print(jsondata)
        x = json.loads(jsondata, object_hook=lambda d: SimpleNamespace(**d))
        print(x)


if __name__ == "__main__":
    unittest.main()
