#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWGraph data type.
"""


class LWWGraph():
    
    def __init__(self):
        pass
    
    def queryVertex(self, vertexId):
        pass
    
    def addVertex(self, vertexId, timestamp: int):
        pass
    
    def removeVertex(self, vertexId, timestamp: int):
        pass
    
    def addEdge(self, sourceVertexId, destinationVertexId, timestamp: int):
        pass
    
    def removeEdge(self, sourceVertexId, destinationVertexId, timestamp: int):
        pass
    
    def clearVertices(self, timestamp: int):
        pass
