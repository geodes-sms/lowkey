#!/usr/bin/env python

from collabtypes.Clock import Clock, ClockMode
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

"""
print(time.time_ns())
halt()
halt()
print(time.time_ns())

"""

Clock.setUp(ClockMode.DEBUG)

mindmap = MindMap('improvePublicationRecord')

# Create CentralTopic and add to the MindMap
centralTopic = CentralTopic('publishPaper')
mindmap.setTopic(centralTopic)

# Create two MainTopics and add them to the CentralTopic
mt1 = MainTopic('experiment')
centralTopic.addMainTopic(mt1)

# Create this one with a missing argument
mt2 = MainTopic()
mt2.setName('writePaper')
centralTopic.addMainTopic(mt2)

# Create two SubTopics and add them to one of the MainTopics
s1 = SubTopic('relatedWork')
mt2.addSubTopic(s1)
s2 = SubTopic('contributions')
mt2.addSubTopic(s2)

# Create a Marker
x = Marker('x')
mindmap.addMarker(x)
s2.setMarker(x)

# Print the MindMap
MindmapPrinter.printMindmap(mindmap)
