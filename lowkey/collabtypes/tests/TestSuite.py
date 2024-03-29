#!/usr/bin/env python
import unittest

from lowkey.collabtypes.tests.ClockTests import ClockTests
from lowkey.collabtypes.tests.ClabjectTests import ClabjectTests
from lowkey.collabtypes.tests.EntityTests import EntityTests

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Full test suite for the modeling layer.
"""


def create_suite():
    testCases = [ClabjectTests, EntityTests, ClockTests]
    loadedCases = []
    
    for case in testCases:
        loadedCases.append(unittest.defaultTestLoader.loadTestsFromTestCase(case))

    return unittest.TestSuite(loadedCases)


if __name__ == '__main__':
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
