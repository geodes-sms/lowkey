#!/usr/bin/env python
import unittest

from collabtypes.Clock import Clock, ClockMode
from mindmap.metamodel.entities.CentralTopic import CentralTopic
from mindmap.metamodel.entities.Marker import Marker
from mindmap.metamodel.entities.MindMap import MindMap
from mindmap.metamodel.entities.MindMapModel import MindMapModel

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
        mindmapModel.addNode(mindmap)
        self.assertEqual(mindmapModel.getNodeById(mindmap.getId()), mindmap)

    def testCreateUpdateRoot(self):
        title1 = "improveTeachingRecord"
        mindmap = MindMap(title1)
        self.assertEqual(mindmap.getTitle(), title1)
        
        title2 = "improvePublicationRecord"
        mindmap.setTitle(title2)
        self.assertEqual(mindmap.getTitle(), title2)
        
    def testCreateRemoveNonAggregationReference(self):
        mindmap = MindMap("improveTeachingRecord")
        centralTopic = CentralTopic("publishPaper")
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
        Clock.setUp(ClockMode.DEBUG)
        
        mindmap = MindMap("improveTeachingRecord")
        topicName = "publishPaper"
        centralTopic = CentralTopic(topicName)
        mindmap.setTopic(centralTopic)
        
        self.assertEqual(mindmap.getTopic().getName(), topicName)
        
        topicName2 = "goToVacation"
        centralTopic2 = CentralTopic(topicName2)
        mindmap.setTopic(centralTopic2)
        
        self.assertEqual(mindmap.getTopic().getName(), topicName2)

        
if __name__ == "__main__":
    unittest.main()
