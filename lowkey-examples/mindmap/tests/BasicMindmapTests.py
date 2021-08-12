#!/usr/bin/env python
import os
import sys
import unittest
import logging

from mindmap.editor.CollabSession import CollabSession
from mindmap.editor.CommandParser import CommandParser

from lowkey.collabtypes.Clock import Clock, ClockMode
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.Marker import Marker
from metamodel.entities.MindMap import MindMap
from metamodel.entities.MindMapModel import MindMapModel

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class BasicMindmapTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(BasicMindmapTests, cls).setUpClass()
        logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.ERROR)
    
    def setUp(self):
        Clock.setUp(ClockMode.DEBUG)
        self._parser = CommandParser()
        self._session = CollabSession()
        self._mindMapModel = self._session._mindmapmodel
        
    def tearDown(self):
        del(self._mindMapModel)
        
    def testCreateModelWithContent(self):
        title1 = "improveTeachingRecord"
        
        command = self._parser.parseMessage("create mindmap {}".format(title1))
        command.execute(self._session)
        
        self.assertEqual(len(self._session._mindmapmodel.getNodes()), 1)
        mindmap = MindMap(self._session._mindmapmodel.getNodes()[0])
        self.assertEqual(mindmap.getTitle(), title1)
        
    '''
    def testCreateModelWithContent(self):
        title1 = "improveTeachingRecord"
        
        mindmap = MindMap(title1)
        mindmap.addToModel(self._mindMapModel)
        
        self.assertEqual(self._mindMapModel.getNodeById(mindmap.getId()), mindmap._clabject)
    
    
    def testCreateUpdateRoot(self):
        title1 = "improveTeachingRecord"
        
        mindmap = MindMap(title1)
        mindmap.addToModel(self._mindMapModel)
        
        self.assertEqual(mindmap.getTitle(), title1)
        
        title2 = "improvePublicationRecord"
        mindmap.setTitle(title2)
        self.assertEqual(mindmap.getTitle(), title2)
    
    def testCreateRemoveNonCompositionReference(self):
        mindmap = MindMap("improveTeachingRecord")
        mindmap.addToModel(self._mindMapModel)
        
        centralTopic = CentralTopic("publishPaper")
        centralTopic.addToModel(self._mindMapModel)
        
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
        mindmap.addToModel(self._mindMapModel)
        
        centralTopic = CentralTopic("publishPaper")
        centralTopic.addToModel(self._mindMapModel)
        mindmap.setTopic(centralTopic)
        
        x = Marker("x")
        x.addToModel(self._mindMapModel)
        mindmap.addMarker(x)
        centralTopic.setMarker(x)
        
        self.assertEqual(centralTopic.getMarker().getSymbol(), "x")
        
        mindmap.removeMarker(x)
        
        
        markerAssociationsOnCurrentMindmap = [a for a in self._mindMapModel.getAssociationsByName("markers") if a.getFrom() == mindmap]
        self.assertFalse(markerAssociationsOnCurrentMindmap)
        self.assertFalse(centralTopic.getMarker())  # TODO: should be False if cascade removal is supported
        
    
    def testCreateUpdateContainedReferenceTarget(self):
        mindmap = MindMap("improveTeachingRecord")
        mindmap.addToModel(self._mindMapModel)
        
        topicName = "publishPaper"
        centralTopic = CentralTopic(topicName)
        centralTopic.addToModel(self._mindMapModel)
        
        mindmap.setTopic(centralTopic)
        self.assertEqual(mindmap.getTopic().getName(), topicName)
        
        topicName2 = "goToVacation"
        centralTopic2 = CentralTopic(topicName2)
        centralTopic2.addToModel(self._mindMapModel)
        
        mindmap.setTopic(centralTopic2)
        
        self.assertEqual(mindmap.getTopic().getName(), topicName2)
        
    def testCreateMainTopic(self):
        mindmap = MindMap("improveTeachingRecord")
        mindmap.addToModel(self._mindMapModel)
        
        topicName = "publishPaper"
        centralTopic = CentralTopic(topicName)
        centralTopic.addToModel(self._mindMapModel)
        
        mindmap.setTopic(centralTopic)
        self.assertEqual(mindmap.getTopic().getName(), topicName)
        
        
        mainTopicName = "processRelatedWork"
        mainTopic = MainTopic(mainTopicName)
        mainTopic.addToModel(self._mindMapModel)
        
        centralTopic.addMainTopic(mainTopic)
        self.assertEqual(centralTopic.getMainTopics()[0].getName(), mainTopicName)
        
        
        mainTopicName2 = "doTheExperiment"
        mainTopic2 = MainTopic(mainTopicName2)
        mainTopic2.addToModel(self._mindMapModel)
        
        centralTopic.addMainTopic(mainTopic2)
        self.assertEqual(centralTopic.getMainTopics()[1].getName(), mainTopicName2)
    '''    


if __name__ == "__main__":
    unittest.main()
