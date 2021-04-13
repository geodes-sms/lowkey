#!/usr/bin/env python
import unittest

from collabtypes.Clock import Clock, ClockMode

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class ClockTests(unittest.TestCase):

    def testClockModeIsSingleton(self):
        clock = Clock.setUp(mode=ClockMode.DEBUG)
        clock2 = Clock.setUp()
        self.assertEqual(clock.getMode(), clock2.getMode())
    
    def testClockModeCannotBeOverridden(self):
        clock = Clock.setUp(mode=ClockMode.DEBUG)
        clock2 = Clock.setUp(mode=ClockMode.REAL)
        self.assertEqual(clock.getMode(), clock2.getMode())
        
    def testDebugClockTicksCorrectly(self):
        clock = Clock.setUp(mode=ClockMode.DEBUG)
        
        currentTime1 = clock.currentTime()
        currentTime2 = clock.currentTime()
        self.assertEqual(abs(currentTime1-currentTime2), clock.getStep())


if __name__ == "__main__":
    unittest.main()
