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
from editor.EditorSession import EditorSession

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

Clock.setUp(ClockMode.DEBUG)

parser = CommandParser()

session1 = EditorSession()
session2 = EditorSession()

commandStack = []

commandStack.extend([
        parser.parseMessage("create mindmap mm1"),
        parser.parseMessage("read")
    ])

for command in commandStack:
    command.execute(session1)

for command in commandStack:
    command.execute(session2)
