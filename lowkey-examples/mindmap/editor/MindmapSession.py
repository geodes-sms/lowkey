#!/usr/bin/env python
import logging
import os
import sys
import uuid

from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabapi.Session import Session

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from metamodel import MindMapPackage
from metamodel.entities.MindMapModel import MindMapModel

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Session object to manage local modeling data.
"""


class MindmapSession(Session):
    
    def __init__(self):
        super().__init__()
        self._mindmapmodel = MindMapModel()
        self.addModel(self._mindmapmodel)
        
    def getMindMapModel(self):
        return self._mindmapmodel
