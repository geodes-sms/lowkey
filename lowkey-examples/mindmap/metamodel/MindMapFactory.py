#!/usr/bin/env python
from entities.CentralTopic import CentralTopic
from entities.MainTopic import MainTopic
from entities.Marker import Marker
from entities.MindMap import MindMap
from entities.SubTopic import SubTopic
from entities.Topic import Topic


__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Factory module for the MindMap metamodel.
"""


# Case insensitive class resolution
def factory(classname, name=""):
    if classname.lower() not in [k.lower() for k in globals().keys()]:
        return None
    klass = {k.lower():v for k, v in globals().items()}[classname]
    return klass()
