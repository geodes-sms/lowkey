__author__ = "Istvan David"
__copyright__ = "Copyright 2021"

"""
Abstract Node type for the general logical type model level. Serves as a common abstraction to the other logical types.
"""

import uuid

class Node:
    
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid1()