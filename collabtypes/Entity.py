__author__ = "Istvan David"
__copyright__ = "Copyright 2021"

"""
Entity type for the general logical type model level.
"""

from .Node import Node

class Entity(Node):
    
    def __init__(self):
        super().__init__()