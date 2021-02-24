#!/usr/bin/env python
import unittest

from lww.LWWGraph import LWWGraph
from lww.LWWSet import LWWSet

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
        self.assertEqual(lwwGraph.size(), 1)
        v1AdjacencySet = lwwGraph.getAdjacencySet(v1)
        self.assertTrue(isinstance(v1AdjacencySet, LWWSet))
        self.assertEqual(v1AdjacencySet.size(), 0)
        
        lwwGraph.addVertex(v1, 20)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertEqual(lwwGraph.size(), 1)
        v1AdjacencySet = lwwGraph.getAdjacencySet(v1)
        self.assertTrue(isinstance(v1AdjacencySet, LWWSet))
        self.assertEqual(v1AdjacencySet.size(), 0)
        
        lwwGraph.addVertex(v2, 30)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertEqual(lwwGraph.size(), 2)
        v1AdjacencySet = lwwGraph.getAdjacencySet(v1)
        v2AdjacencySet = lwwGraph.getAdjacencySet(v2)
        self.assertTrue(isinstance(v1AdjacencySet, LWWSet))
        self.assertTrue(isinstance(v2AdjacencySet, LWWSet))
        self.assertEqual(v1AdjacencySet.size(), 0)
        self.assertEqual(v2AdjacencySet.size(), 0)
        
    def testAddEdgeToExistingVertices(self):
        lwwGraph = LWWGraph()
        
        v1 = "A"
        v2 = "B"
        e = "edgeAtoB"
        
        lwwGraph.addVertex(v1, 10)
        lwwGraph.addVertex(v2, 20)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        
        lwwGraph.addEdge(e, v1, v2, 30)
        self.assertEqual(lwwGraph.size(), 2)
        v1AdjacencySet = lwwGraph.getAdjacencySet(v1)
        v2AdjacencySet = lwwGraph.getAdjacencySet(v2)
        self.assertTrue(isinstance(v1AdjacencySet, LWWSet))
        self.assertTrue(isinstance(v2AdjacencySet, LWWSet))
        self.assertEqual(v1AdjacencySet.size(), 1)
        self.assertEqual(v2AdjacencySet.size(), 0)
        
        
if __name__ == "__main__":
    unittest.main()
