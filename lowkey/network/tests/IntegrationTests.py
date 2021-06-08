#!/usr/bin/env python
import json
import logging
import time
import unittest

from network.Session import Session

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Integration tests for distributed clients.

Prerequisites:
-Start a proxy.
-Start a subscriber.
"""


class IntegrationTests(unittest.TestCase):

    def testBasicWorkflow(self):
        logging.basicConfig(level=logging.INFO)
        session = Session()
        session.join(address='127.0.0.1', xsubPort='5566', xpubPort='5567')
        self.assertNotEqual(session, None)
        
        """
        Give time to the ZMQ elements being set up. Might require higher values in real distributed
        settings. A synchronous setup workflow might be more appropriate here. 
        """
        time.sleep(.5)
        
        session.createEntity("entity1")
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
