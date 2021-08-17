#!/usr/bin/env python
import os
import sys
import unittest
import logging

from mindmap.editor.DSLParser import DSLParser
from mindmap.editor.MindmapSession import MindmapSession

from lowkey.collabtypes.Clock import Clock, ClockMode
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.Marker import Marker
from metamodel.entities.MindMap import MindMap
from metamodel.entities.MindMapModel import MindMapModel
from metamodel import MindMapPackage

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
        self._parser = DSLParser()
        self._session = MindmapSession()
        
    def tearDown(self):
        del(self._session)
        del(self._parser)
        
    def testCreateModelWithContent(self):
        title1 = "improvePublicationRecord"
        message = "create MindMap {}".format(title1)
        
        command = self._parser.translateIntoCollabAPICommand(message)
        self._session.processMessage(command)
        
        self.assertEqual(len(self._session.getMindMapModel().getNodes()), 1)
        mindmap = MindMap(self._session.getMindMapModel().getNodes()[0])
        self.assertEqual(mindmap.getTitle(), title1)
    
    def testCreateUpdateRoot(self):
        title1 = "improvePublicationRecord"
        message = "create MindMap {}".format(title1)
        
        command = self._parser.translateIntoCollabAPICommand(message)
        self._session.processMessage(command)
        
        self.assertEqual(len(self._session.getMindMapModel().getNodes()), 1)
        mindmap = MindMap(self._session.getMindMapModel().getNodes()[0])
        self.assertEqual(mindmap.getTitle(), title1)
        
        title2 = "improveTeachingRecord"
        mindmap.setTitle(title2)
        self.assertEqual(mindmap.getTitle(), title2)
    
    def testCreateRemoveNonCompositionReference(self):
        messages = []
        
        messages.extend([
            "create MindMap improvePublicationRecord",
            "create CentralTopic publishPaper",
            "link improvePublicationRecord.topic to publishPaper",
            "create Marker x",
            "link publishPaper.marker to x",
            ])
        
        for message in messages:
            command = self._parser.translateIntoCollabAPICommand(message)
            self._session.processMessage(command)
        
        centralTopic = CentralTopic(self._session.getMindMapModel().getNodesByType(MindMapPackage.TYPES.CENTRAL_TOPIC)[0])
        
        self.assertEqual(Marker(centralTopic.getMarker()).getSymbol(), "x")
        
        centralTopic.removeMarker()
        self.assertFalse(centralTopic.getMarker())
    
    @unittest.skip("The DSL should be fixed by adding the UpdateAssociationCommand")
    def testCreateUpdateContainedReferenceTarget(self):
        commands = []
        
        topic1Name = "publishPaper"
        
        commands.extend([
            self._parser.parseMessage("create mindmap improvePublicationRecord"),
            self._parser.parseMessage("create centraltopic {}".format(topic1Name)),
            self._parser.parseMessage("link {} to improvePublicationRecord.topic".format(topic1Name))
            ])
        
        for command in commands:
            command.execute(self._session)
        
        mindmap = MindMap(self._session._mindmapmodel.getNodesByType(MindMapPackage.TYPES.MINDMAP)[0])
        self.assertEqual(mindmap.getTopic().getName(), topic1Name)
        
        commands = []
        
        topic2Name = "goToVacation"
        
        commands.extend([
            self._parser.parseMessage("create centraltopic {}".format(topic2Name)),
            self._parser.parseMessage("link {} to improvePublicationRecord.topic".format(topic2Name))
        ])
        
        self.assertEqual(mindmap.getTopic().getName(), topic2Name)
    
    def testCreateMainTopic(self):
        messages = []
        
        centralTopicName = "publishPaper"
        mainTopic1Name = "processRelatedWork"
        mainTopic2Name = "doTheExperiment"
        
        messages.extend([
            "create MindMap improvePublicationRecord",
            "create CentralTopic {}".format(centralTopicName),
            "link improvePublicationRecord.topic to {}".format(centralTopicName),
            "create MainTopic {}".format(mainTopic1Name),
            "create MainTopic {}".format(mainTopic2Name),
            "link {}.maintopics to {}".format(centralTopicName, mainTopic1Name),
            "link {}.maintopics to {}".format(centralTopicName, mainTopic2Name),
            ])
        
        for message in messages:
            command = self._parser.translateIntoCollabAPICommand(message)
            self._session.processMessage(command)
            
        mindmap = MindMap(self._session.getMindMapModel().getNodesByType(MindMapPackage.TYPES.MINDMAP)[0])
        centralTopic = CentralTopic(self._session.getMindMapModel().getNodesByType(MindMapPackage.TYPES.CENTRAL_TOPIC)[0])
        
        self.assertEqual(mindmap.getTopic().getName(), centralTopicName)
        self.assertEqual(centralTopic.getMainTopics()[0].getName(), mainTopic1Name)
        self.assertEqual(centralTopic.getMainTopics()[1].getName(), mainTopic2Name)


if __name__ == "__main__":
    unittest.main()
