#!/usr/bin/env python
from _ast import arguments
import uuid

from mindmap.metamodel import MindMapFactory

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Session object for collaboration.
"""


class Session():
    
    def __init__(self):
        self.__id = uuid.uuid1()
        self.__model = None
        
    def create(self, arguments):
        assert(len(arguments) == 2)
        klass = arguments[0]
        name = arguments[1]
        instance = MindMapFactory.factory(klass, name)
        
        if not instance:
            return None
        
        self.__model = instance
        
        print(self.__model)
    
    def read(self, arguments):
        pass
    
    def update(self, arguments):
        pass
    
    def delete(self, arguments):
        pass
