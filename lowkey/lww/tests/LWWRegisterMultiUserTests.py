#!/usr/bin/env python
import unittest

from lww.LWWRegister import LWWRegister

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWRegisterMultiUserTests(unittest.TestCase):
    
    def testTwoActors(self):
        lwwRegisterA = LWWRegister()
        lwwRegisterB = LWWRegister()
        
        """
        t=10
        Actor A updates his register.
        Due to the network delay, this message will be propagated to B at t=20.
        """
        valueA = "New value set by A."
        lwwRegisterA.update(valueA, 10)
        
        """
        t=15
        Actor B updates his register.
        Due to the network delay, this message will be propagated to A at t=25.
        """
        valueB = "New value set by B."
        lwwRegisterB.update(valueB, 15)
        
        """
        t=20
        A's message reaches B with the original timestamp.
        """
        lwwRegisterB.update(valueA, 10)
        
        """
        t=25
        B's message reaches A with the original timestamp.
        """
        lwwRegisterA.update(valueB, 15)
        
        self.assertEqual(lwwRegisterA.query(), valueB)
        self.assertEqual(lwwRegisterB.query(), valueB)
        

if __name__ == "__main__":
    unittest.main()
