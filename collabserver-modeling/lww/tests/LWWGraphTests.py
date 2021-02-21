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
        self.assertEqual(lwwGraph.queryVertex(v1), v1)
        self.assertEqual(lwwGraph.getVertexes().size(), 1)
        
        lwwGraph.addVertex(v1, 10)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertEqual(lwwGraph.queryVertex(v1), v1)
        self.assertEqual(lwwGraph.getVertexes().size(), 1)
        
        lwwGraph.addVertex(v2, 20)
        self.assertTrue(lwwGraph.vertexExists(v1))
        self.assertTrue(lwwGraph.vertexExists(v2))
        self.assertEqual(lwwGraph.queryVertex(v1), v1)
        self.assertEqual(lwwGraph.queryVertex(v2), v2)
        self.assertEqual(lwwGraph.getVertexes().size(), 2)
        

if __name__ == "__main__":
    unittest.main()
