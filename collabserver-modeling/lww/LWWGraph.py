#!/usr/bin/env python
from lww.LWWMap import LWWMap
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
        self.__adjacencyMap = LWWMap()
    
    """Interface methods: accessors"""
        
    def size(self):
        return self.__adjacencyMap.size()
    
    """Interface methods: vertices"""

    def vertexExists(self, vertex) -> bool:
        return self.__adjacencyMap.exists(vertex)
    
    def getAdjacencySet(self, vertex):
        return self.__adjacencyMap.query(vertex)
    
    def addVertex(self, vertex, timestamp: int):
        return self.__adjacencyMap.add(vertex, LWWSet(), timestamp)
    
    def removeVertex(self, vertex, timestamp: int):
        pass
    
    """Interface methods: edges"""

    def edgeExists(self, edge) -> bool:
        pass
    
    def queryEdge(self, edge):
        pass
    
    def addEdge(self, edge, sourceVertex, destinationVertex, timestamp: int):
        if not self.vertexExists(sourceVertex):
            raise KeyError("Source vertex does not exist.")
        if not self.vertexExists(destinationVertex):
            raise KeyError("Destination vertex does not exist.")
        
        self.getAdjacencySet(sourceVertex).add(edge, timestamp)
    
    def addEdgeByVertexId(self, edge, sourceVertexId, destinationVertexId, timestamp: int):
        pass
    
    def removeEdge(self, sourceVertexId, destinationVertexId, timestamp: int):
        pass
