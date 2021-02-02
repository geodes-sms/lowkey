__author__ = "Istvan David"
__copyright__ = "Copyright 2021"

"""
Abstract Node type for the general logical type model level. Serves as a common abstraction to the other logical types.
"""

import uuid

class Node:
    
    def __init__(self):
        self.__id = uuid.uuid1()
        
    def getId(self):
        return self.__id
        
    #Attribute handling
    def attributeGetter(f):
        def decoratedAttributeGetter(self):
            '''
            TODO: query CollabServer for an updated value at this point
            and potantially establish caching
            '''
            return f(self)
        return decoratedAttributeGetter
    
    def attributeSetter(f):
        def decoratedAttributeSetter(self, node):
            '''
            TODO: push the new value to CollabServer at this point
            '''
            f(self, node)
        return decoratedAttributeSetter