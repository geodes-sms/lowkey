#!/usr/bin/env python
import uuid

from metamodel.entities.MindMap import MindMap
from metamodel.entities.CentralTopic import CentralTopic
import logging
from lowkey.collabtypes.Clabject import Clabject
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.SubTopic import SubTopic
from editor import MindMapPackage

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Session object to manage local modeling data.
"""


class EditorSession():
    
    def __init__(self):
        self._id = uuid.uuid1()
        self._mindmap = MindMap()
        self._tmp = []
    
    def classFactory(self, classname):
        if classname.lower() not in [k.lower() for k in globals().keys()]:
            return None
        klass = {k.lower():v for k, v in globals().items()}[classname.lower()]
        return klass()
    
    def integrateClabject(self, clabject):
        logging.debug(clabject)
        logging.debug(" Integrating clabject {} ({})'.".format(clabject.getName(), clabject.getType()))
        if(isinstance(clabject, CentralTopic)):
            logging.debug(">>integrating as centraltopic")
            self._mindmap.setTopic(clabject)
        elif(isinstance(clabject, MainTopic)):
            logging.debug(">>integrating as maintopic")
            centralTopic = self._mindmap.getTopic()
            centralTopic.addMainTopic(clabject)
        elif(isinstance(clabject, SubTopic)):
            logging.debug(">>integrating as subtopic")
            self._tmp.append(clabject)
            print(self._tmp)
            logging.debug("Clabject added to _tmp")
        else:
            logging.debug("Unexpected type")
            
    def integrateAssociation(self, association):
        logging.debug(association)
        associationName = association.getName()
        fromClabject = association.getFrom()
        toClabject = association.getTo()
        logging.debug(" Integrating association '{}' between {} and {}.".format(associationName, fromClabject, toClabject))
        
        print(self._tmp)
        
        st = None
        
        for e in self._tmp:
            print("printing e")
            print(e)
            print(e.getName())
            print(toClabject)
            if e.getName() == toClabject:
                st = e
                break
        
        print(st)
        
        ct = self._mindmap.getTopic()
        for mt in ct.getMainTopics():
            if mt.getName() == fromClabject:
                mt.addSubTopic(st)
                self._tmp.remove(st)