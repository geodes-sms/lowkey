#!/usr/bin/env python
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
        self.__nodes = []
    
    # Node handling
    def _getNodes(self):
        return self.__nodes
        
    def _addNode(self, node):
        self.__nodes.append(node)
    
    def _removeNode(self, node):
        if(node in self.__nodes):
            self.__nodes.remove(node)
        # Here, this should trigger a cascade delete on every reference,
        # since this is the composite aggregation that contains the node in the model.
        
    def _setNode(self, oldNode, newNode):
        self._removeNode(oldNode)
        self._addNode(newNode)
