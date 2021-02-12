#!/usr/bin/env python
import unittest

from lww.LWWStack import LWWStack

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWStackTests(unittest.TestCase):
    
    def testPush(self):
        lwwStack = LWWStack()
        lwwStack.push("message 1", 10)
        self.assertEqual(lwwStack.peek().query(), "message 1")
        lwwStack.push("message 2", 20)
        
        for x in lwwStack.getContents():
            print(x.getTimestamp())
        
        self.assertEqual(lwwStack.peek().query(), "message 2")
        self.assertEqual(lwwStack.pop().query(), "message 2")
        self.assertEqual(lwwStack.pop().query(), "message 1")
        with self.assertRaises(IndexError):
            lwwStack.pop()

            
if __name__ == "__main__":
    unittest.main()
