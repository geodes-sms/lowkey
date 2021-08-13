#!/usr/bin/env python
import unittest

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from lowkey.collabtypes.Clock import Clock, ClockMode
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Entity import Entity
from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Model import Model
from metamodel import MindMapPackage

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class CollabtypesMindmapTests(unittest.TestCase):
    
    def setUp(self):
        Clock.setUp(ClockMode.DEBUG)
        self._mindMapModel = Model()
        
    def tearDown(self):
        del(self._mindMapModel)
        
    def testCreateModelWithContent(self):
        title1 = "improvePublicationRecord"
        
        mindmap = Clabject()
        mindmap.setType(MindMapPackage.TYPES.MINDMAP)
        mindmap.setAttribute(MindMapPackage.TITLE, title1)
        mindmap.addToModel(self._mindMapModel)
        
        self.assertTrue(mindmap in self._mindMapModel.getNodesByType(MindMapPackage.TYPES.MINDMAP))
    
    def testCreateUpdateRoot(self):
        title1 = "improvePublicationRecord"
        
        mindmap = Clabject()
        mindmap.setType(MindMapPackage.TYPES.MINDMAP)
        mindmap.setAttribute(MindMapPackage.TITLE, title1)
        mindmap.addToModel(self._mindMapModel)
        
        self.assertEqual(mindmap.getAttribute(MindMapPackage.TITLE), title1)
        
        title2 = "improvePublicationRecord"
        mindmap.setAttribute(MindMapPackage.TITLE, title2)
        self.assertEqual(mindmap.getAttribute(MindMapPackage.TITLE), title2)
    
    def testCreateRemoveNonCompositionReference(self):
        mindmap = Clabject()
        mindmap.setType(MindMapPackage.TYPES.MINDMAP)
        mindmap.setAttribute(MindMapPackage.TITLE, "improvePublicationRecord")
        mindmap.addToModel(self._mindMapModel)
        
        centralTopic = Clabject()
        centralTopic.setType(MindMapPackage.TYPES.CENTRAL_TOPIC)
        centralTopic.setName("publishPaper")
        centralTopic.addToModel(self._mindMapModel)
        
        self.assertEqual(len(self._mindMapModel.getNodes()), 2)
        self.assertTrue(mindmap in self._mindMapModel.getNodes())
        self.assertTrue(centralTopic in self._mindMapModel.getNodes())
        
        topicLink = Association()
        topicLink.setFrom(mindmap)
        topicLink.setTo(centralTopic)
        topicLink.setName(MindMapPackage.ASSOCIATION_MINDMAP_CENTRALTOPIC)
        topicLink.addToModel(self._mindMapModel)
        
        self.assertEqual(len(self._mindMapModel.getNodes()), 3)
        self.assertTrue(mindmap in self._mindMapModel.getNodes())
        self.assertTrue(centralTopic in self._mindMapModel.getNodes())
        self.assertTrue(topicLink in self._mindMapModel.getNodes())
        self.assertTrue(topicLink in self._mindMapModel.getAssociations())
        
        mindmapEntity = Entity(mindmap)
        self.assertEqual(len(mindmapEntity.getAssociations()), 1)
        self.assertEqual(mindmapEntity.getAssociations()[0].getFrom(), mindmap)
        self.assertEqual(mindmapEntity.getAssociations()[0].getTo(), centralTopic)
        
    def testCreateUpdateContainedReferenceTarget(self):
        mindmap = Clabject()
        mindmap.setType(MindMapPackage.TYPES.MINDMAP)
        mindmap.setAttribute(MindMapPackage.TITLE, "improvePublicationRecord")
        mindmap.addToModel(self._mindMapModel) 
        
        topicName = "publishPaper"
        centralTopic = Clabject()
        centralTopic.setType(MindMapPackage.TYPES.CENTRAL_TOPIC)
        centralTopic.setName(topicName)
        centralTopic.addToModel(self._mindMapModel)
        
        topicLink = Association()
        topicLink.setFrom(mindmap)
        topicLink.setTo(centralTopic)
        topicLink.setName(MindMapPackage.ASSOCIATION_MINDMAP_CENTRALTOPIC)
        topicLink.addToModel(self._mindMapModel)
        
        mindmapEntity = Entity(mindmap)
        self.assertEqual(len(mindmapEntity.getAssociations()), 1)
        self.assertEqual(mindmapEntity.getAssociations()[0].getFrom(), mindmap)
        self.assertEqual(mindmapEntity.getAssociations()[0].getTo(), centralTopic)
        
        topicName2 = "goToVacation"
        centralTopic2 = Clabject()
        centralTopic2.setType(MindMapPackage.TYPES.CENTRAL_TOPIC)
        centralTopic2.setName(topicName2)
        centralTopic2.addToModel(self._mindMapModel)
        
        topicLink.setTo(centralTopic2)
        self.assertEqual(mindmapEntity.getAssociations()[0].getTo(), centralTopic2)
    
    '''    
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
