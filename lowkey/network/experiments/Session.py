#!/usr/bin/env python
import uuid

from collabtypes.Entity import Entity
from collabtypes.Model import Model

from network.Publisher import Publisher

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Session with a collection of LWW-level data.
"""


class Session(object):

    def __init__(self):
        self.id = uuid.uuid1()    
        self.model = Model()
    
    def join(self, address='127.0.0.1', xsubPort='5566', xpubPort='5567'):
        print('SESSION: creating publisher')
        self.publisher = Publisher(address=address, port=xsubPort)
        print('SESSION: created publisher')
        # print('SESSION: creating sub')
        # self.subscriber = Subscriber(address=address, port=xpubPort)
        # print('SESSION: created sub')
    
    def getEntity(self, name):
        return self.model.getNodeByName(name)
    
    def createEntity(self, name):
        entity = Entity()
        entity.setName(name)
        
        self.model.addNode(entity)
        
        self.syncAll("CREATE {}".format(entity.getName()))
    
    def syncAll(self, message):
        self.publisher.sendMessage(message)
