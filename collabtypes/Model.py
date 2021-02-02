__author__ = "Istvan David"
__copyright__ = "Copyright 2021"

"""
Model type for the general logical type model level.
"""

from .Node import Node

class Model(Node):
    
    def __init__(self):
        super().__init__()
        self.__nodes = []
    
    #Node handling
    def getNodes(self):
        return self.__nodes
        
    def __addNode(self, node):
        self.__nodes.append(node)
        
    def __removeNode(self, node):
        self.__nodes.remove(node)
        #Here, this should trigger a cascade delete on every reference, since this is the composite aggregation that contains the node in the model.

    #In both 0..1 and 0..* cases
    def nodeAdder(f):
        def decoratedNodeAdder(self, node):
            self.__addNode(node)
            f(self, node)
        return decoratedNodeAdder
    
    #In a 0..1 case
    def nodeSetter(f):
        def decoratedNodeSetter(self, node):
            self.__addNode(node)    #here, the behaviour should be >replace oldNode with newNode
            f(self, node)
        return decoratedNodeSetter
    
    #In a 0..* case
    def nodeRemover(f):
        def decoratedNodeRemover(self, node):
            self.__removeNode(node)
            f(self, node)
        return decoratedNodeRemover