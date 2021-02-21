#!/usr/bin/env python
from lww.LWWSet import LWWSet

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWGraph data type.
"""


class LWWGraph():
    
    def __init__(self):
        self.__verteces = LWWSet()
        self.__edges = LWWSet()
    
    """Interface methods: accessors"""
        
    def getVertexes(self):
        return self.__verteces
    
    def getEdges(self):
        return self.__edges
    
    """Interface methods: vertices"""

    def vertexExists(self, vertex) -> bool:
        return self.__verteces.exists(vertex)
    
    def queryVertex(self, vertex):
        return self.__verteces.query(vertex)
    
    def addVertex(self, vertex, timestamp: int):
        return self.__verteces.add(vertex, timestamp)
    
    def removeVertex(self, vertex, timestamp: int):
        pass
    
    """Interface methods: edges"""

    def edgeExists(self, edge) -> bool:
        return self.__edges.exists(edge)
    
    def queryEdge(self, edge):
        return self.__edges.query(edge)
    
    def addEdge(self, sourceVertexId, destinationVertexId, timestamp: int):
        pass
    
    def removeEdge(self, sourceVertexId, destinationVertexId, timestamp: int):
        pass