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
from editor.CommandParser import CommandParser
from editor.CollabSession import CollabSession

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

Clock.setUp(ClockMode.DEBUG)

parser = CommandParser()

session1 = CollabSession()
session2 = CollabSession()

commandStack = []

commandStack.extend([
        parser.parseMessage("create mindmap mm1"),
        #parser.parseMessage("read")
    ])

for command in commandStack:
    command.execute(session1)
'''
for command in commandStack:
    command.execute(session2)
'''

commandStack = []
commandStack.extend([
        parser.parseMessage("create centraltopic c1"),
        parser.parseMessage("link c1 to mm1.topic"),
        #parser.parseMessage("objects"),
        #parser.parseMessage("read")
    ])

for command in commandStack:
    command.execute(session1)
    
    
commandStack = []
commandStack.extend([
        parser.parseMessage("create maintopic m1"),
        parser.parseMessage("link m1 to c1.maintopics"),
        parser.parseMessage("create subtopic s1"),
        parser.parseMessage("link s1 to m1.subtopics"),
        parser.parseMessage("create marker x"),
        parser.parseMessage("link x to s1.marker"),
        parser.parseMessage("read")
    ])

for command in commandStack:
    command.execute(session1)