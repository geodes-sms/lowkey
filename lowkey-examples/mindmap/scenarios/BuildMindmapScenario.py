#!/usr/bin/env python
import time
import unittest

from mindmap import MindmapPrinter
from mindmap.metamodel.entities.CentralTopic import CentralTopic
from mindmap.metamodel.entities.MainTopic import MainTopic
from mindmap.metamodel.entities.Marker import Marker
from mindmap.metamodel.entities.MindMap import MindMap
from mindmap.metamodel.entities.SubTopic import SubTopic

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


def halt():
    time.sleep(0.001)


class BuildMindmapScenario(unittest.TestCase):

    def testBuildMindmap(self): 
        # Create MindMap
        title = 'improveTeachingRecord'
        mindmap = MindMap(title)
        halt()
        
        self.assertEqual(mindmap.getTitle(), title)
        
        newTitle = 'improvePublicationRecord'
        mindmap.setTitle(newTitle)
        halt()
        self.assertEqual(mindmap.getTitle(), newTitle)
        
        # Create CentralTopic and add to the MindMap
        centralTopicName = 'publishPaper'
        centralTopic = CentralTopic(centralTopicName)
        mindmap.setTopic(centralTopic)
        halt()
        self.assertEqual(centralTopic.getName(), centralTopicName)
        
        self.assertEqual(mindmap.getTopic(), centralTopic)
        self.assertEqual(mindmap.getTopic().getName(), centralTopicName)
        
        """
        # Create two MainTopics and add them to the CentralTopic
        mt1 = MainTopic('experiment')
        c.addMainTopic(mt1)
        halt()
        
        # #Create this one with a missing argument
        mt2 = MainTopic()
        mt2.setName('writePaper')
        halt()
        c.addMainTopic(mt2)
        halt()
        
        # Create two SubTopics and add them to one of the MainTopics
        s1 = SubTopic('relatedWork')
        mt2.addSubTopic(s1)
        halt()
        s2 = SubTopic('contributions')
        mt2.addSubTopic(s2)
        halt()
        
        # Create a Marker
        x = Marker('x')
        mindmap.addMarker(x)
        halt()
        s2.setMarker(x)
        halt()
        """
        # Print the MindMap
        # MindmapPrinter.printMindmap(mindmap)

        
if __name__ == "__main__":
    unittest.main()
