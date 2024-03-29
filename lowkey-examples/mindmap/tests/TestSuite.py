#!/usr/bin/env python
import os
import sys
import unittest

from mindmap.tests.BasicMindmapTests import BasicMindmapTests
from mindmap.tests.CollabtypesMindmapTests import CollabtypesMindmapTests
from mindmap.tests.DSLParserTests import DSLParserTests
from mindmap.tests.NetworkedMindmapTests import NetworkedMindmapTests

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Full test suite for the Mindmap example.
"""


def create_suite():
    testCases = [DSLParserTests, BasicMindmapTests, CollabtypesMindmapTests, NetworkedMindmapTests]
    loadedCases = []
    
    for case in testCases:
        loadedCases.append(unittest.defaultTestLoader.loadTestsFromTestCase(case))    

    return unittest.TestSuite(loadedCases)


if __name__ == '__main__':
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
