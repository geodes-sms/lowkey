#!/usr/bin/env python
from lowkey.collabtypes import Literals
from lowkey.lww.LWWGraph import LWWGraph

from .Node import Node

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Model type for the general logical type model level.
"""


class Model(Node):
    
    def __init__(self):
        super().__init__()
        self.persistence = LWWGraph()
        self.setAttribute(Literals.NODES, ())
    
    # Nodes CRUD
    def addNode(self, node:Node):
        nodes = self.getAttribute(Literals.NODES)
        nodes = nodes + (node,)
        return self.updateAttribute(Literals.NODES, nodes)
    
    def getNodes(self):
        return self.getAttribute(Literals.NODES)
        
    def getNodeByName(self, name:str):
        nodes = self.getNodes()
        return next(n for n in nodes if n.getAttribute(Literals.NAME) == name)  # names should be unique
    
    def getNodeById(self, identifier):
        nodes = self.getNodes()
        return next(n for n in nodes if n.getId() == identifier)  # IDs should be unique
    
    def removeNode(self, node:Node):
        nodes = self.getAttribute(Literals.NODES)
        remainingNodes = ()
        for n in nodes:
            if n != node:
                remainingNodes = remainingNodes + (n,)
        
        self.updateAttribute(Literals.NODES, remainingNodes)
        
    def updateNode(self, oldNode:Node, newNode:Node):
        self.removeNode(oldNode)
        self.addNode(newNode)
