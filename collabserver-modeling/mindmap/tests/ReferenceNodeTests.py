#!/usr/bin/env python
import unittest

from mindmap.metamodel.entities.CentralTopic import CentralTopic
from mindmap.metamodel.entities.Marker import Marker
from mindmap.metamodel.entities.MindMap import MindMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class ReferenceNodeTests(unittest.TestCase):
    
    def testSetting01ReferenceAddsANode(self):
        mindmap = MindMap('improvePublicationRecord')
        
        # Create CentralTopic and add to the MindMap
        centralTopic = CentralTopic('publishPaper')
        mindmap.setTopic(centralTopic)
        
        self.assertTrue(centralTopic in mindmap._getNodes())
        
    def testUpdating01ReferenceAddsNewNodeAndRemovesPreviousNode(self):
        mindmap = MindMap('improvePublicationRecord')
        
        # Create CentralTopic and add to the MindMap
        centralTopic = CentralTopic('publishPaper')
        mindmap.setTopic(centralTopic)
        
        self.assertTrue(centralTopic in mindmap._getNodes())
        
        # Create new CentralTopic and add to the MindMap
        centralTopic2 = CentralTopic('goToVacation')
        mindmap.setTopic(centralTopic2)
        
        self.assertFalse(centralTopic in mindmap._getNodes())
        self.assertTrue(centralTopic2 in mindmap._getNodes())

    def testAdding0NReferenceAddsAllNodes(self):
        mindmap = MindMap('improvePublicationRecord')
                
        # Create a Marker
        marker = Marker('x')
        mindmap.addMarker(marker)
        
        self.assertTrue(marker in mindmap._getNodes())
        
        # Create a Marker
        marker2 = Marker('*')
        mindmap.addMarker(marker2)
        
        self.assertTrue(marker in mindmap._getNodes())
        self.assertTrue(marker2 in mindmap._getNodes())


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
