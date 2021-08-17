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
from mindmap.tests.NetworkStub import NetworkStub

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class NetworkedMindmapTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(NetworkedMindmapTests, cls).setUpClass()
        logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.ERROR)
    
    def setUp(self):
        Clock.setUp(ClockMode.DEBUG)
        self._dslParser = DSLParser()
        self._localSession = MindmapSession()
        self._remoteSession = MindmapSession()
        self._network = NetworkStub(self._localSession, self._remoteSession)
        self._sessions = [self._localSession, self._remoteSession]
        
    def tearDown(self):
        del(self._localSession)
        del(self._remoteSession)
        del(self._dslParser)
        del(self._network)
        
    def testCreateModelWithContent(self):
        title1 = "improvePublicationRecord"
        
        message = "create MindMap {}".format(title1)
        
        #localCommand = self._dslParser.parseMessage(message)
        collabCommand = self._dslParser.translateIntoCollabAPICommand(message)
        
        self._localSession.processMessage(collabCommand)
        #localCommand.execute(self._localSession)
        
        self._network.forward(collabCommand)
    
        self.assertEqual(len(self._localSession.getMindMapModel().getNodes()), 1)
        mindmap = MindMap(self._localSession.getMindMapModel().getNodes()[0])
        self.assertEqual(mindmap.getTitle(), title1)
        
        self.assertEqual(len(self._remoteSession.getMindMapModel().getNodes()), 1)
        mindmap = MindMap(self._remoteSession.getMindMapModel().getNodes()[0])
        self.assertEqual(mindmap.getTitle(), title1)
            
    '''
    def testCreateUpdateRoot(self):
        title1 = "improvePublicationRecord"
        
        command = self._parser.parseMessage("create mindmap {}".format(title1))
        command.execute(self._session)
        
        self.assertEqual(len(self._session.getMindMapModel().getNodes()), 1)
        mindmap = MindMap(self._session.getMindMapModel().getNodes()[0])
        self.assertEqual(mindmap.getTitle(), title1)
        
        title2 = "improveTeachingRecord"
        mindmap.setTitle(title2)
        self.assertEqual(mindmap.getTitle(), title2)
    
    def testCreateRemoveNonCompositionReference(self):
        commands = []
        
        commands.extend([
            self._parser.parseMessage("create mindmap improvePublicationRecord"),
            self._parser.parseMessage("create centraltopic publishPaper"),
            self._parser.parseMessage("link publishPaper to improvePublicationRecord.topic"),
            self._parser.parseMessage("create marker x"),
            self._parser.parseMessage("link x to publishPaper.marker"),
            ])
        
        for command in commands:
            command.execute(self._session)
        
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
        commands = []
        
        centralTopicName = "publishPaper"
        mainTopic1Name = "processRelatedWork"
        mainTopic2Name = "doTheExperiment"
        
        commands.extend([
            self._parser.parseMessage("create mindmap improvePublicationRecord"),
            self._parser.parseMessage("create centraltopic {}".format(centralTopicName)),
            self._parser.parseMessage("link {} to improvePublicationRecord.topic".format(centralTopicName)),
            self._parser.parseMessage("create maintopic {}".format(mainTopic1Name)),
            self._parser.parseMessage("create maintopic {}".format(mainTopic2Name)),
            self._parser.parseMessage("link {} to {}.maintopics".format(mainTopic1Name, centralTopicName)),
            self._parser.parseMessage("link {} to {}.maintopics".format(mainTopic2Name, centralTopicName)),
            ])
        
        for command in commands:
            command.execute(self._session)
            
        mindmap = MindMap(self._session.getMindMapModel().getNodesByType(MindMapPackage.TYPES.MINDMAP)[0])
        centralTopic = CentralTopic(self._session.getMindMapModel().getNodesByType(MindMapPackage.TYPES.CENTRAL_TOPIC)[0])
        
        self.assertEqual(mindmap.getTopic().getName(), centralTopicName)
        self.assertEqual(centralTopic.getMainTopics()[0].getName(), mainTopic1Name)
        self.assertEqual(centralTopic.getMainTopics()[1].getName(), mainTopic2Name)
        
    '''    


if __name__ == "__main__":
    unittest.main()
