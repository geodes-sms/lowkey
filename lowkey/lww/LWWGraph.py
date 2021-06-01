#!/usr/bin/env python
from lww.LWWEdge import LWWEdge
from lww.LWWMap import LWWMap
from lww.LWWSet import LWWSet
from lww.LWWVertex import LWWVertex

_author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
LWWGraph data type, based on the 2P2PGraph specification in
https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf.
"""


class LWWGraph(LWWMap):
    
    def __init__(self):
        super().__init__()
        self.__vertices = LWWSet()  # set of (LWWVertex, timestamp) tuples
        self.__edges = LWWSet()  # set of (LWWEdge, timestamp) tuples        
    
    """Interface methods: accessors"""
        
    def numberOfVertices(self):
        return self.__vertices.size()
    
    """Interface methods: vertices"""

    def vertexExists(self, vertex:LWWVertex) -> bool:
        return self.__vertices.lookup(vertex)
    
    def getAdjacencyListForVertex(self, vertex:LWWVertex):
        adjacentVertices = []
        for edge, _timestamp in self.__edges:
            if edge.query("from") == vertex:
                adjacentVertices.append(edge.query("to"))
        return adjacentVertices
    
    def addVertex(self, vertex:LWWVertex, timestamp: int):
        return self.__vertices.add(vertex, timestamp)
    
    """Precedence is given to this operation, as discussed in the specification."""

    def removeVertex(self, vertex:LWWVertex, timestamp: int):
        if self.__vertexIsSourceOfEdge(vertex) or self.__vertexIsDestinationOfEdge(vertex):
            raise Exception
        else:
            self.__vertices.remove(vertex, timestamp) 
    
    def __vertexIsSourceOfEdge(self, vertex:LWWVertex):
        for edge, _timestamp in self.__edges:
            if edge.query("from") == vertex:
                return True
        return False
    
    def __vertexIsDestinationOfEdge(self, vertex:LWWVertex):
        for edge, _timestamp in self.__edges:
            if edge.query("to") == vertex:
                return True
        return False
    
    """Interface methods: edges"""
    
    def edgeExists(self, edge) -> bool:
        return True if self.__queryEdgeByName(edge.query("name")) else False
    
    def edgeExistsWithName(self, edgeName) -> bool:
        return True if self.__queryEdgeByName(edgeName) else False
   
    def nodeExists(self, node):
        return self.vertexExists(node) or node == self
     
    def addEdgeWithName(self, edgeName, sourceNode, destinationNode, timestamp: int):
        if not self.nodeExists(sourceNode):
            raise KeyError("Source vertex does not exist.")
        if not self.nodeExists(destinationNode):
            raise KeyError("Destination vertex does not exist.")
        
        edge = LWWEdge()
        edge.add("name", edgeName)
        edge.add("from", sourceNode)
        edge.add("to", destinationNode)
        
        self.__edges.add(edge, timestamp)
        
    def addEdge(self, edge:LWWEdge, timestamp: int):
        if not self.nodeExists(edge.query("from")):
            raise KeyError("Source vertex does not exist.")
        if not self.nodeExists(edge.query("to")):
            raise KeyError("Destination vertex does not exist.")
        
        self.__edges.add(edge, timestamp)
    
    def removeEdgeByName(self, edgeName, timestamp: int):
        edge = self.__queryEdgeByName(edgeName)
        if not edge:
            raise Exception("Edge does not exist")
        
        self.removeEdge(edge, timestamp)
    
    def removeEdge(self, edge, timestamp):
        if not self.__queryEdgeByName(edge.query("name")):
            raise Exception("Edge does not exist")
        self.__edges.remove(edge, timestamp)
    
    """Internal methods"""
        
    def __queryEdgeByName(self, edgeName):
        for edge, _timestamp in self.__edges:
            if edge.query("name") == edgeName:
                return edge
            
        return None
