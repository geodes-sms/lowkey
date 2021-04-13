#!/usr/bin/env python
from lww.LWWSet import LWWSet

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWGraph data type, based on the 2P2PGraph specification in
https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.
"""


class Edge():
    
    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Edge):
            return self.__id == other.getId()
        return False
    
    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))
    
    def __init__(self, edgeId, destinationVertex):
        self.__id = edgeId
        self.__destinationVertex = destinationVertex
    
    def getId(self):
        return self.__id
    
    def getDestinationVertex(self):
        return self.__destinationVertex


class LWWGraph():
    
    def __init__(self):
        self.__vertices = LWWSet()  # set of vertices
        self.__edges = LWWSet()  # set of (edgeId, sourceVertex, destinationVertex) tuples
        # TODO: this tuple might not be handled correctly in the LWWSet (see: _lookupFunction)
    
    """Interface methods: accessors"""
        
    def numberOfVertices(self):
        return self.__vertices.size()
    
    """Interface methods: vertices"""

    def vertexExists(self, vertex) -> bool:
        return self.__vertices.lookup(vertex)
    
    def getAdjacencyListForVertex(self, vertex):
        adjacentVertices = []
        for edgeData, _timestamp in self.__edges:
            if edgeData[1] == vertex:
                adjacentVertices.append(edgeData[2])
        return adjacentVertices
    
    def addVertex(self, vertex, timestamp: int):
        return self.__vertices.add(vertex, timestamp)
    
    """Precedence is given to this operation, as discussed in the specification."""

    def removeVertex(self, vertex, timestamp: int):
        if self.__vertexIsSourceOfEdge(vertex) or self.__vertexIsDestinationOfEdge(vertex):
            raise Exception
        else:
            self.__vertices.remove(vertex, timestamp) 
    
    def __vertexIsSourceOfEdge(self, vertex):
        for edgeData, _timestamp in self.__edges:
            if edgeData[1] == vertex:
                return True
        return False
    
    def __vertexIsDestinationOfEdge(self, vertex):
        for edgeData, _timestamp in self.__edges:
            if edgeData[2] == vertex:
                return True
        return False
    
    """Interface methods: edges"""
    
    def edgeExists(self, edgeId) -> bool:
        return True if self.__queryEdge(edgeId) else False
        
    def addEdge(self, edgeId, sourceVertex, destinationVertex, timestamp: int):
        if not self.vertexExists(sourceVertex):
            raise KeyError("Source vertex does not exist.")
        if not self.vertexExists(destinationVertex):
            raise KeyError("Destination vertex does not exist.")
        
        self.__edges.add((edgeId, sourceVertex, destinationVertex), timestamp)
    
    def removeEdge(self, edgeId, timestamp: int):
        edge = self.__queryEdge(edgeId)
        if not edge:
            raise Exception("Edge does not exist")
        
        self.__edges.remove(edge, timestamp)
    
    """Internal methods"""
        
    def __queryEdge(self, edgeId):
        for edgeData, _timestamp in self.__edges:
            if edgeData[0] == edgeId:
                return edgeData
            
        return None
