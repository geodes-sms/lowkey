#!/usr/bin/env python
import uuid

from metamodel.entities.MindMap import MindMap
from metamodel.entities.CentralTopic import CentralTopic
import logging
from lowkey.collabtypes.Entity import Entity
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
    
    def integrateEntity(self, entity):
        logging.debug(entity)
        logging.debug(" Integrating entity {} ({})'.".format(entity.getName(), entity.getType()))
        if(isinstance(entity, CentralTopic)):
            logging.debug(">>integrating as centraltopic")
            self._mindmap.setTopic(entity)
        elif(isinstance(entity, MainTopic)):
            logging.debug(">>integrating as maintopic")
            centralTopic = self._mindmap.getTopic()
            centralTopic.addMainTopic(entity)
        elif(isinstance(entity, SubTopic)):
            logging.debug(">>integrating as subtopic")
            self._tmp.append(entity)
            print(self._tmp)
            logging.debug("Entity added to _tmp")
        else:
            logging.debug("Unexpected type")
            
    def integrateRelationship(self, relationship):
        logging.debug(relationship)
        relationshipName = relationship.getName()
        fromEntity = relationship.getFrom()
        toEntity = relationship.getTo()
        logging.debug(" Integrating relationship '{}' between {} and {}.".format(relationshipName, fromEntity, toEntity))
        
        print(self._tmp)
        
        st = None
        
        for e in self._tmp:
            print("printing e")
            print(e)
            print(e.getName())
            print(toEntity)
            if e.getName() == toEntity:
                st = e
                break
        
        print(st)
        
        ct = self._mindmap.getTopic()
        for mt in ct.getMainTopics():
            if mt.getName() == fromEntity:
                mt.addSubTopic(st)
                self._tmp.remove(st)