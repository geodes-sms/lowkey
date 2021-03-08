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
        self.__adjacencyMap = LWWMap()
    
    """Interface methods: accessors"""
        
    def numberOfVertices(self):
        return self.__adjacencyMap.size()
    
    """Interface methods: vertices"""

    def vertexExists(self, vertex) -> bool:
        return self.__adjacencyMap.exists(vertex)
    
    def getAdjacencySet(self, vertex) -> LWWSet:
        return self.__adjacencyMap.query(vertex)
    
    def addVertex(self, vertex, timestamp: int):
        return self.__adjacencyMap.add(vertex, LWWSet(), timestamp)
    
    def removeVertex(self, vertex, timestamp: int):
        if self.__vertexIsSourceOfEdge(vertex) or self.__vertexIsDestinationOfEdge(vertex):
            raise Exception
        else:
            self.__adjacencyMap.remove(vertex, timestamp) 
    
    def __vertexIsSourceOfEdge(self, vertex):
        return True if self.getAdjacencySet(vertex).size() > 0 else False
    
    def __vertexIsDestinationOfEdge(self, vertex):
        for _vertex, adjacencySet in self.__adjacencyMap.entrySet():
            for edge in adjacencySet:
                if edge.getDestinationVertex() == vertex:
                    return True
        return False
    
    """Interface methods: edges"""

    def edgeExists(self, edgeId) -> bool:
        return True if self.queryEdge(edgeId) else False
            
    def queryEdge(self, edgeId):
        for _vertex, adjacencySet in self.__adjacencyMap.entrySet():
            for edge in adjacencySet:
                if edge.getId() == edgeId:
                    return edge, adjacencySet
            
        return None
    
    def addEdge(self, edgeId, sourceVertex, destinationVertex, timestamp: int):
        if not self.vertexExists(sourceVertex):
            raise KeyError("Source vertex does not exist.")
        if not self.vertexExists(destinationVertex):
            raise KeyError("Destination vertex does not exist.")
        
        self.getAdjacencySet(sourceVertex).add(Edge(edgeId, destinationVertex), timestamp)
    
    def removeEdge(self, edgeId, timestamp: int):
        edge, adjacencySet = self.queryEdge(edgeId)
        if edge:
            adjacencySet.remove(Edge(edgeId, edge.getDestinationVertex()), timestamp)
