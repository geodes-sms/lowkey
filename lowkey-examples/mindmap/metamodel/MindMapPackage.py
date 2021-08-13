#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""


class TYPES():
    """TYPES"""
    MINDMAP = "MindMap"
    CENTRAL_TOPIC = "CentralTopic"
    MAIN_TOPIC = "MainTopic"
    SUBTOPIC = "SubTopic"
    MARKER = "Marker"
    TYPES = [MINDMAP, CENTRAL_TOPIC, MAIN_TOPIC, SUBTOPIC, MARKER]

"""LITERALS"""
ASSOCIATION_MINDMAP_CENTRALTOPIC = "topic"
ASSOCIATION_MINDMAP_MARKER = "markers"
ASSOCIATION_CENTRALTOPIC_MAINTOPIC = "maintopics"
ASSOCIATION_MAINTOPIC_SUBTOPIC = "subtopics"
ASSOCIATION_SUBTOPIC_SUBTOPIC = "subtopics"
ASSOCIATION_TOPIC_MARKER = "marker"
MARKER_SYMBOL = "symbol"
TITLE = "title"
