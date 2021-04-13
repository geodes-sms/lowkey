#!/usr/bin/env python
import unittest

from lww.LWWGraph import LWWGraph

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class LWWGrapTests(unittest.TestCase):

    def testAddVertices(self):
        lwwGraph = LWWGraph()
        
        v1 = "A"
        v2 = "B"
        
        lwwGraph.addVertex(v1, 10)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertEqual(lwwGraph.numberOfVertices(), 1)
        v1AdjacencySet = lwwGraph.getAdjacencySetForVertex(v1)
        self.assertEqual(len(v1AdjacencySet), 0)
        
        lwwGraph.addVertex(v1, 20)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertEqual(lwwGraph.numberOfVertices(), 1)
        v1AdjacencySet = lwwGraph.getAdjacencySetForVertex(v1)
        self.assertEqual(len(v1AdjacencySet), 0)
        
        lwwGraph.addVertex(v2, 30)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertEqual(lwwGraph.numberOfVertices(), 2)
        v1AdjacencySet = lwwGraph.getAdjacencySetForVertex(v1)
        v2AdjacencySet = lwwGraph.getAdjacencySetForVertex(v2)
        self.assertEqual(len(v1AdjacencySet), 0)
        self.assertEqual(len(v2AdjacencySet), 0)
    
    def testAddEdgesToExistingVertices(self):
        lwwGraph = LWWGraph()
        
        v1 = "A"
        v2 = "B"
        e1 = "edgeAtoB"
        e2 = "edgeAtoB_2"
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
        lwwGraph.addEdge(e1, v1, v2, 30)
        self.assertEqual(lwwGraph.numberOfVertices(), 2)
        self.assertTrue(lwwGraph.edgeExists(e1))
        v1AdjacencySet = lwwGraph.getAdjacencySetForVertex(v1)
        v2AdjacencySet = lwwGraph.getAdjacencySetForVertex(v2)
        self.assertEqual(len(v1AdjacencySet), 1)
        self.assertEqual(len(v2AdjacencySet), 0)
        
        lwwGraph.addEdge(e2, v1, v2, 30)
        self.assertEqual(lwwGraph.numberOfVertices(), 2)
        self.assertTrue(lwwGraph.edgeExists(e1))
        self.assertTrue(lwwGraph.edgeExists(e2))
        v1AdjacencySet = lwwGraph.getAdjacencySetForVertex(v1)
        v2AdjacencySet = lwwGraph.getAdjacencySetForVertex(v2)
        self.assertEqual(len(v1AdjacencySet), 2)
        self.assertEqual(len(v2AdjacencySet), 0)
        
    def testDirectedEdgeHandling(self):
        lwwGraph = LWWGraph()
        
        v1 = "A"
        v2 = "B"
        e1 = "edgeAtoB"
        e2 = "edgeBtoA"
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
        lwwGraph.addEdge(e1, v1, v2, 30)
        self.assertEqual(lwwGraph.numberOfVertices(), 2)
        self.assertTrue(lwwGraph.edgeExists(e1))
        v1AdjacencySet = lwwGraph.getAdjacencySetForVertex(v1)
        v2AdjacencySet = lwwGraph.getAdjacencySetForVertex(v2)
        self.assertEqual(len(v1AdjacencySet), 1)
        self.assertEqual(len(v2AdjacencySet), 0)
        
        lwwGraph.addEdge(e2, v2, v1, 30)
        self.assertEqual(lwwGraph.numberOfVertices(), 2)
        self.assertTrue(lwwGraph.edgeExists(e1))
        self.assertTrue(lwwGraph.edgeExists(e2))
        v1AdjacencySet = lwwGraph.getAdjacencySetForVertex(v1)
        v2AdjacencySet = lwwGraph.getAdjacencySetForVertex(v2)
        self.assertEqual(len(v1AdjacencySet), 1)
        self.assertEqual(len(v2AdjacencySet), 1)
    
    def testAddEdgeToNonExistingSource(self):
        lwwGraph = LWWGraph()
        
        v1 = "A"
        v2 = "B"
        e = "edgeAtoB"
        
        lwwGraph.addVertex(v2, 10)
        self.assertFalse(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
        self.assertRaises(KeyError, lwwGraph.addEdge, e, v1, v2, 30)
        
    def testAddEdgeToNonExistingDestination(self):
        lwwGraph = LWWGraph()
        
        v1 = "A"
        v2 = "B"
        e = "edgeAtoB"
        
        lwwGraph.addVertex(v1, 10)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertFalse(lwwGraph.vertexExists(v2))
        
        self.assertRaises(KeyError, lwwGraph.addEdge, e, v1, v2, 30)
    
    def testRemoveExistingEdge(self):
        lwwGraph = LWWGraph()
        
        v1 = "A"
        v2 = "B"
        e = "edgeAtoB"
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        lwwGraph.addEdge(e, v1, v2, 30)
        
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertTrue(lwwGraph.edgeExists(e))
        
        lwwGraph.removeEdge(e, 40)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertFalse(lwwGraph.edgeExists(e))
    
    def testRemoveNonExistingEdge(self):
        lwwGraph = LWWGraph()
        
        v1 = "A"
        v2 = "B"
        e = "edgeAtoB"
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertFalse(lwwGraph.edgeExists(e))
        
        self.assertRaises(Exception, lwwGraph.removeEdge, e, 40)
        
    def testRemoveVertexWithoutEdges(self):
        lwwGraph = LWWGraph()
        
        v1 = "A"
        v2 = "B"
        
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
        
        v1 = "A"
        v2 = "B"
        e = "edgeAtoB"
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        lwwGraph.addEdge(e, v1, v2, 30)
        
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertTrue(lwwGraph.edgeExists(e))
        
        self.assertRaises(Exception, lwwGraph.removeVertex, v1, 30)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
    def testRemoveVertexWithIncomingEdge(self):
        lwwGraph = LWWGraph()
        
        v1 = "A"
        v2 = "B"
        e = "edgeAtoB"
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        lwwGraph.addEdge(e, v1, v2, 30)
        
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertTrue(lwwGraph.edgeExists(e))
        
        self.assertRaises(Exception, lwwGraph.removeVertex, v2, 40)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))

        
if __name__ == "__main__":
    unittest.main()
