#!/usr/bin/env python
import unittest

from lww.tests.LWWRegisterMultiUserTests import LWWRegisterMultiUserTests
from lww.tests.LWWRegisterTests import LWWRegisterTests
from lww.tests.LWWSetTests import LWWSetTests
from lww.tests.EmbeddingTests import EmbeddingTests
from lww.tests.LWWMapTests import LWWMapTests

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Full test suite for the LWW implementations.
"""

def create_suite():
    testCases = [LWWRegisterTests, LWWRegisterMultiUserTests, LWWSetTests, LWWMapTests, EmbeddingTests]
    loadedCases = []
    
    for case in testCases:
        loadedCases.append(unittest.defaultTestLoader.loadTestsFromTestCase(case))    

    return unittest.TestSuite(loadedCases)

if __name__ == '__main__':
    suite = create_suite()
    runner=unittest.TextTestRunner()
    runner.run(suite)
