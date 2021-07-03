#!/usr/bin/env python
import unittest

from lowkey.lww.LWWEdge import LWWEdge
from lowkey.lww.LWWGraph import LWWGraph
from lowkey.lww.LWWVertex import LWWVertex

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWGrapTests(unittest.TestCase):

    def testAddVertices(self):
        lwwGraph = LWWGraph()
        
        v1Name = "A"
        v2Name = "B"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 5)
        v2 = LWWVertex()
        v2.add("name", v2Name, 6)
        
        lwwGraph.addVertex(v1, 10)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertEqual(lwwGraph.numberOfVertices(), 1)
        v1AdjacencySet = lwwGraph.getAdjacencyListForVertex(v1)
        self.assertEqual(len(v1AdjacencySet), 0)
        
        lwwGraph.addVertex(v1, 20)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertEqual(lwwGraph.numberOfVertices(), 1)
        v1AdjacencySet = lwwGraph.getAdjacencyListForVertex(v1)
        self.assertEqual(len(v1AdjacencySet), 0)
        
        lwwGraph.addVertex(v2, 30)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertEqual(lwwGraph.numberOfVertices(), 2)
        v1AdjacencySet = lwwGraph.getAdjacencyListForVertex(v1)
        v2AdjacencySet = lwwGraph.getAdjacencyListForVertex(v2)
        self.assertEqual(len(v1AdjacencySet), 0)
        self.assertEqual(len(v2AdjacencySet), 0)
    
    def testAddEdgesToExistingVertices(self):
        lwwGraph = LWWGraph()
        
        v1Name = "A"
        v2Name = "B"
        e1Name = "edgeAtoB"
        e2Name = "edgeAtoB_2"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 1)
        v2 = LWWVertex()
        v2.add("name", v2Name, 2)
        
        e1 = LWWEdge()
        e1.add("name", e1Name, 3)
        e1.add("from", v1, 3)
        e1.add("to", v2, 3)
        
        e2 = LWWEdge()
        e2.add("name", e2Name, 4)
        e2.add("from", v1, 4)
        e2.add("to", v2, 4)
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
        lwwGraph.addEdge(e1, 30)
        self.assertEqual(lwwGraph.numberOfVertices(), 2)
        self.assertTrue(lwwGraph.edgeExists(e1))
        v1AdjacencySet = lwwGraph.getAdjacencyListForVertex(v1)
        v2AdjacencySet = lwwGraph.getAdjacencyListForVertex(v2)
        self.assertEqual(len(v1AdjacencySet), 1)
        self.assertEqual(len(v2AdjacencySet), 0)
        
        lwwGraph.addEdge(e2, 30)
        self.assertEqual(lwwGraph.numberOfVertices(), 2)
        self.assertTrue(lwwGraph.edgeExists(e1))
        self.assertTrue(lwwGraph.edgeExists(e2))
        v1AdjacencySet = lwwGraph.getAdjacencyListForVertex(v1)
        v2AdjacencySet = lwwGraph.getAdjacencyListForVertex(v2)
        self.assertEqual(len(v1AdjacencySet), 2)
        self.assertEqual(len(v2AdjacencySet), 0)
        
    def testDirectedEdgeHandling(self):
        lwwGraph = LWWGraph()
        
        v1Name = "A"
        v2Name = "B"
        e1Name = "edgeAtoB"
        e2Name = "edgeBtoA"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 1)
        v2 = LWWVertex()
        v2.add("name", v2Name, 2)
        
        e1 = LWWEdge()
        e1.add("name", e1Name, 3)
        e1.add("from", v1, 3)
        e1.add("to", v2, 3)
        
        e2 = LWWEdge()
        e2.add("name", e2Name, 4)
        e2.add("from", v2, 4)
        e2.add("to", v1, 4)
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
        lwwGraph.addEdge(e1, 30)
        self.assertEqual(lwwGraph.numberOfVertices(), 2)
        self.assertTrue(lwwGraph.edgeExists(e1))
        v1AdjacencySet = lwwGraph.getAdjacencyListForVertex(v1)
        v2AdjacencySet = lwwGraph.getAdjacencyListForVertex(v2)
        self.assertEqual(len(v1AdjacencySet), 1)
        self.assertEqual(len(v2AdjacencySet), 0)
        
        lwwGraph.addEdge(e2, 30)
        self.assertEqual(lwwGraph.numberOfVertices(), 2)
        self.assertTrue(lwwGraph.edgeExists(e1))
        self.assertTrue(lwwGraph.edgeExists(e2))
        v1AdjacencySet = lwwGraph.getAdjacencyListForVertex(v1)
        v2AdjacencySet = lwwGraph.getAdjacencyListForVertex(v2)
        self.assertEqual(len(v1AdjacencySet), 1)
        self.assertEqual(len(v2AdjacencySet), 1)
    
    def testAddEdgeToNonExistingSource(self):
        lwwGraph = LWWGraph()
        
        v1Name = "A"
        v2Name = "B"
        e1Name = "edgeAtoB"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 1)
        v2 = LWWVertex()
        v2.add("name", v2Name, 2)
        
        e1 = LWWEdge()
        e1.add("name", e1Name, 3)
        e1.add("from", v1, 3)
        e1.add("to", v2, 3)
        
        lwwGraph.addVertex(v2, 10)
        self.assertFalse(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
        self.assertRaises(KeyError, lwwGraph.addEdge, e1, 30)
        
    def testAddEdgeToNonExistingDestination(self):
        lwwGraph = LWWGraph()
        
        v1Name = "A"
        v2Name = "B"
        e1Name = "edgeAtoB"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 1)
        v2 = LWWVertex()
        v2.add("name", v2Name, 2)
        
        e1 = LWWEdge()
        e1.add("name", e1Name, 3)
        e1.add("from", v1, 3)
        e1.add("to", v2, 3)
        
        lwwGraph.addVertex(v1, 10)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertFalse(lwwGraph.vertexExists(v2))
        
        self.assertRaises(KeyError, lwwGraph.addEdge, e1, 30)
    
    def testRemoveExistingEdge(self):
        lwwGraph = LWWGraph()
        
        v1Name = "A"
        v2Name = "B"
        e1Name = "edgeAtoB"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 1)
        v2 = LWWVertex()
        v2.add("name", v2Name, 2)
        
        e1 = LWWEdge()
        e1.add("name", e1Name, 3)
        e1.add("from", v1, 3)
        e1.add("to", v2, 3)
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        lwwGraph.addEdge(e1, 30)
        
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertTrue(lwwGraph.edgeExists(e1))
        
        lwwGraph.removeEdge(e1, 40)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertFalse(lwwGraph.edgeExists(e1))
    
    def testRemoveNonExistingEdge(self):
        lwwGraph = LWWGraph()
        
        v1Name = "A"
        v2Name = "B"
        e1Name = "edgeAtoB"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 1)
        v2 = LWWVertex()
        v2.add("name", v2Name, 2)
        
        e1 = LWWEdge()
        e1.add("name", e1Name, 3)
        e1.add("from", v1, 3)
        e1.add("to", v2, 3)
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertFalse(lwwGraph.edgeExists(e1))
        
        self.assertRaises(Exception, lwwGraph.removeEdge, e1, 40)
        
    def testRemoveVertexWithoutEdges(self):
        lwwGraph = LWWGraph()
        
        v1Name = "A"
        v2Name = "B"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 1)
        v2 = LWWVertex()
        v2.add("name", v2Name, 2)
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
        lwwGraph.removeVertex(v1, 30)
        self.assertFalse(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
        lwwGraph.removeVertex(v2, 40)
        self.assertFalse(lwwGraph.vertexExists(v1))
        self.assertFalse(lwwGraph.vertexExists(v2))
        
    def testRemoveVertexWithOutgoingEdge(self):
        lwwGraph = LWWGraph()
        
        v1Name = "A"
        v2Name = "B"
        e1Name = "edgeAtoB"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 1)
        v2 = LWWVertex()
        v2.add("name", v2Name, 2)
        
        e1 = LWWEdge()
        e1.add("name", e1Name, 3)
        e1.add("from", v1, 3)
        e1.add("to", v2, 3)
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        lwwGraph.addEdge(e1, 30)
        
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertTrue(lwwGraph.edgeExists(e1))
        
        self.assertRaises(Exception, lwwGraph.removeVertex, v1, 30)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
    def testRemoveVertexWithIncomingEdge(self):
        lwwGraph = LWWGraph()
        
        v1Name = "A"
        v2Name = "B"
        e1Name = "edgeAtoB"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 1)
        v2 = LWWVertex()
        v2.add("name", v2Name, 2)
        
        e1 = LWWEdge()
        e1.add("name", e1Name, 3)
        e1.add("from", v1, 3)
        e1.add("to", v2, 3)
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        lwwGraph.addEdge(e1, 30)
        
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertTrue(lwwGraph.edgeExists(e1))
        
        self.assertRaises(Exception, lwwGraph.removeVertex, v2, 40)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
    def testGraphAsEdgeEndpoint(self):
        lwwGraph = LWWGraph()
        lwwGraph.add("name", "root", 1)
        
        v1Name = "A"
        e1Name = "edgeRootToA"
        
        v1 = LWWVertex()
        v1.add("name", v1Name, 2)
        
        e1 = LWWEdge()
        e1.add("name", e1Name, 3)
        e1.add("from", lwwGraph, 3)
        e1.add("to", v1, 3)
        
        lwwGraph.addVertex(v1, 10)
        self.assertTrue(lwwGraph.vertexExists(v1))
        
        lwwGraph.addEdge(e1, 30)
        self.assertEqual(lwwGraph.numberOfVertices(), 1)
        self.assertTrue(lwwGraph.edgeExists(e1))
        v1AdjacencySet = lwwGraph.getAdjacencyListForVertex(v1)
        self.assertEqual(len(v1AdjacencySet), 0)
        graphVirtualAdjacencySet = lwwGraph.getAdjacencyListForVertex(lwwGraph)
        self.assertEqual(len(graphVirtualAdjacencySet), 1)
        
if __name__ == "__main__":
    unittest.main()
