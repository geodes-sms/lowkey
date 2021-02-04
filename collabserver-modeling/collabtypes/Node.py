#!/usr/bin/env python
import uuid

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Abstract Node type for the general logical type model level.

Serves as a common abstraction to the other logical types.
"""


class Node:
    
    def __init__(self):
        self.__id = uuid.uuid1()
        
    def getId(self):
        return self.__id
        
    # Attribute handling
    def _getAttribute(self):
        '''
        TODO: query CollabServer for an updated value at this point
        and potantially establish caching
        '''
        pass
    
    def _setAttribute(self):
        '''
        TODO: push the new value to CollabServer at this point
        '''
        pass
