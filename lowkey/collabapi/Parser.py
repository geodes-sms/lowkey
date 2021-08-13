#!/usr/bin/env python
from lowkey.collabtypes.Clabject import Clabject

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Parser for the Collab API.
"""


class Parser():
    
    def createClabject(self, name, type):
        clabject = Clabject()
        clabject.setName(name)
        clabject.setType(type)
        
    def setAttribute(self, clabjectId, attributeName, value):
        clabject = findClabjectById(clabjectId)
        clabject.setAttribute(attributeName, value)
