#!/usr/bin/env python
import uuid

from lowkey.lww.LWWMap import LWWMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Session object to manage local modeling data.
"""


class LWWSession():
    
    def __init__(self):
        self._id = uuid.uuid1()
        self._lwwData = []
        
    def createEntity(self, _type, _name):
        lwwMap = LWWMap()
        lwwMap.add("type", _type, 10)
        lwwMap.add("name", _name, 10)
        self._lwwData.append(lwwMap)
        
    def createRelationship(self, _name, _from, _to):
        lwwMap = LWWMap()
        lwwMap.add("name", _name, 10)
        lwwMap.add("from", _from, 10)
        lwwMap.add("to", _to, 10)
        self._lwwData.append(lwwMap)
