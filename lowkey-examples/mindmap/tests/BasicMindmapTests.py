#!/usr/bin/env python
import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from lowkey.collabtypes.Clock import Clock, ClockMode
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.Marker import Marker
from metamodel.entities.MindMap import MindMap
from metamodel.entities.MindMapModel import MindMapModel

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class BasicMindmapTests(unittest.TestCase):
    
    def setUp(self):
        Clock.setUp(ClockMode.DEBUG)
        
    def testCreateModelWithContent(self):
        mindmapModel = MindMapModel()
        title1 = "improveTeachingRecord"
        
        mindmap = MindMap(title1)
        mindmap.addToModel(mindmapModel)
        
        self.assertEqual(mindmapModel.getNodeById(mindmap.getId()), mindmap)
    
    def testCreateUpdateRoot(self):
        mindmapModel = MindMapModel()
        title1 = "improveTeachingRecord"
        
        mindmap = MindMap(title1)
        mindmap.addToModel(mindmapModel)
        
        self.assertEqual(mindmap.getTitle(), title1)
        
        title2 = "improvePublicationRecord"
        mindmap.setTitle(title2)
        self.assertEqual(mindmap.getTitle(), title2)

    def testCreateRemoveNonCompositionReference(self):
        mindmapModel = MindMapModel()
        
        mindmap = MindMap("improveTeachingRecord")
        mindmap.addToModel(mindmapModel)
        
        centralTopic = CentralTopic("publishPaper")
        centralTopic.addToModel(mindmapModel)
        
        mindmap.setTopic(centralTopic)
        
        x = Marker("x")
        mindmap.addMarker(x)
        centralTopic.setMarker(x)
        
        self.assertEqual(centralTopic.getMarker().getSymbol(), "x")
        
        centralTopic.removeMarker()
        self.assertFalse(centralTopic.getMarker())
    
    
    @unittest.skip("Design choice pending")    
    def testCreateRemoveAggregationReference(self):
        mindmap = MindMap("improveTeachingRecord")
        centralTopic = CentralTopic("publishPaper")
        mindmap.setTopic(centralTopic)
        
        x = Marker("x")
        mindmap.addMarker(x)
        centralTopic.setMarker(x)
        
        self.assertEqual(centralTopic.getMarker().getSymbol(), "x")
        
        mindmap.removeMarker(x)
        self.assertFalse(centralTopic.getMarker())  # TODO: design choice -- should the Marker exist here?
        
    def testCreateUpdateContainedReferenceTarget(self):
        mindmapModel = MindMapModel()
                
        mindmap = MindMap("improveTeachingRecord")
        mindmap.addToModel(mindmapModel)
        
        topicName = "publishPaper"
        centralTopic = CentralTopic(topicName)
        centralTopic.addToModel(mindmapModel)
        
        mindmap.setTopic(centralTopic)
        self.assertEqual(mindmap.getTopic().getName(), topicName)
        
        topicName2 = "goToVacation"
        centralTopic2 = CentralTopic(topicName2)
        centralTopic.addToModel(mindmapModel)
        
        mindmap.setTopic(centralTopic2)
        
        self.assertEqual(mindmap.getTopic().getName(), topicName2)
        
if __name__ == "__main__":
    unittest.main()
