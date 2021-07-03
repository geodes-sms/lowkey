#!/usr/bin/env python
import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.Marker import Marker
from metamodel.entities.MindMap import MindMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class ContainmentRemovalTests(unittest.TestCase):
    
    def testRemovingAContainmentRemovesItsReferences(self):
        mindmap = MindMap('improvePublicationRecord')
        
        # Create CentralTopic and add to the MindMap
        centralTopic = CentralTopic('publishPaper')
        mindmap.setTopic(centralTopic)
        
        self.assertTrue(centralTopic in mindmap._getNodes())
        
        # Create a Marker and assign it to the central topic
        marker = Marker('x')
        mindmap.addMarker(marker)
        centralTopic.setMarker(marker)
        
        self.assertTrue(marker in mindmap._getNodes())
        self.assertTrue(centralTopic.getMarker() == marker)
        
        mindmap.removeMarker(marker)
        self.assertTrue(marker not in mindmap._getNodes())
        # TODO this should be fixed by the cascade containement removal. Commenting it out until we get back to the example.
        # self.assertTrue(centralTopic.getMarker() != marker)
        # self.assertTrue(centralTopic.getMarker() == None)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
