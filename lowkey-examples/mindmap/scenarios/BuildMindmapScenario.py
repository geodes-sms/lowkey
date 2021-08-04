#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from lowkey.collabtypes.Clock import Clock, ClockMode
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.Marker import Marker
from metamodel.entities.MindMap import MindMap
from metamodel.entities.MindMapModel import MindMapModel
from metamodel.entities.SubTopic import SubTopic
from scenarios import PrintHelper

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

Clock.setUp(ClockMode.DEBUG)

mindMapModel = MindMapModel('mindmapModel')

mindmap = MindMap('improvePublicationRecord')
mindmap.addToModel(mindMapModel)


# Create CentralTopic and add to the MindMap
centralTopic = CentralTopic('publishPaper')
centralTopic.addToModel(mindMapModel)
mindmap.setTopic(centralTopic)


# Create two MainTopics and add them to the CentralTopic
mt1 = MainTopic('experiment')
mt1.addToModel(mindMapModel)
centralTopic.addMainTopic(mt1)

# Create this one with a missing argument
mt2 = MainTopic()
mt2.setName('writePaper')
mt2.addToModel(mindMapModel)
centralTopic.addMainTopic(mt2)


# Create two SubTopics and add them to one of the MainTopics
s1 = SubTopic('relatedWork')
s1.addToModel(mindMapModel)
mt2.addSubTopic(s1)
s2 = SubTopic('contributions')
s2.addToModel(mindMapModel)
mt2.addSubTopic(s2)


# Create a Marker
markerX = Marker('x')
markerX.addToModel(mindMapModel)
mindmap.addMarker(markerX)
s2.setMarker(markerX)

# Print the MindMap
PrintHelper.printMindmap(mindmap)



# Create another Marker and add it to the model, but not to the mindmap
markerPlus = Marker('+')
mindMapModel.addNode(markerPlus)

print("\n>added new Marker (+) to the model")

# Print model nodes
PrintHelper.printMindmap(mindmap)
PrintHelper.printModel(mindMapModel)

# Add Marker to the mindmap
mindmap.addMarker(markerPlus)
s1.setMarker(markerPlus)

print("\n>added Marker + to the mindmap")

# Print model nodes
PrintHelper.printMindmap(mindmap)
PrintHelper.printModel(mindMapModel)