#!/usr/bin/env python
import uuid

from metamodel.entities.MindMap import MindMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Session object to manage local modeling data.
"""


class EditorSession():
    
    def __init__(self):
        self._id = uuid.uuid1()
        self._mindmap = MindMap()