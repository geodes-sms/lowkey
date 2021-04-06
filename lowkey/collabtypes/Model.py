#!/usr/bin/env python
from collabtypes import Literals

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
        self.add(Literals.NODES, (), self._currentTime())
    
    # Nodes CRUD
    def _addNode(self, node:Node):
        nodes = self.query(Literals.NODES)
        nodes = nodes + (node,)
        return self.update(Literals.NODES, nodes, self._currentTime())
        
    def _getNode(self, name:str) -> Node:
        nodes = self.query(Literals.NODES)
        return [n for n in nodes if n._getAttribute(Literals.NAME) == name]
    
    def _removeNode(self, node:Node):
        nodes = self.query(Literals.NODES)
        for n in nodes:
            if n == node:
                self.remove(n, self._currentTime())
        # Here, this should trigger a cascade delete on every reference,
        # since this is the composite aggregation that contains the node in the model.
        
    def _updateNode(self, oldNode:Node, newNode:Node):
        self._removeNode(oldNode)
        self._addNode(newNode)
