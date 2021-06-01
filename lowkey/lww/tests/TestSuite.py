#!/usr/bin/env python
import unittest

from lww.tests.EmbeddingTests import EmbeddingTests
from lww.tests.LWWGraphPartsTests import LWWGraphPartsTests
from lww.tests.LWWGraphTests import LWWGrapTests
from lww.tests.LWWMapTests import LWWMapTests
from lww.tests.LWWRegisterMultiUserTests import LWWRegisterMultiUserTests
from lww.tests.LWWRegisterTests import LWWRegisterTests
from lww.tests.LWWSetTests import LWWSetTests
from lww.tests.CloningTests import CloningTests

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Full test suite for the LWW implementations.
"""


def create_suite():
    typeTestCases = [LWWRegisterTests, LWWSetTests, LWWMapTests, LWWGrapTests, LWWGraphPartsTests]
    typeUsageTestCases = [LWWRegisterMultiUserTests, EmbeddingTests]
    behavioralTestCases = [CloningTests]
    loadedCases = []
    
    for case in typeTestCases + typeUsageTestCases + behavioralTestCases:
        loadedCases.append(unittest.defaultTestLoader.loadTestsFromTestCase(case))    

    return unittest.TestSuite(loadedCases)


if __name__ == '__main__':
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
