#!/usr/bin/env python
import unittest

import os
import sys

from mindmap.tests.BasicMindmapTests import BasicMindmapTests
from mindmap.tests.CollabtypesMindmapTests import CollabtypesMindmapTests

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Full test suite for the Mindmap example.
"""


def create_suite():
    testCases = [BasicMindmapTests, CollabtypesMindmapTests]
    loadedCases = []
    
    for case in testCases:
        loadedCases.append(unittest.defaultTestLoader.loadTestsFromTestCase(case))    

    return unittest.TestSuite(loadedCases)


if __name__ == '__main__':
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
