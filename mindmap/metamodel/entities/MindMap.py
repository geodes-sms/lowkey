from collabtypes.Model import Model
from collabtypes.Node import Node

class MindMap(Model):
    
    def __init__(self, title):
        super().__init__()
        self.__title = title
        self.__topic = None
        self.__markers = []

    #Title: attribute
    #getter, setter
    @Node.attributeGetter
    def getTitle(self):
        return self.__title

    @Node.attributeSetter
    def setTitle(self, title):
        self.__title = title
    
    #Topic: 0..1 reference
    #getter, setter
    def getTopic(self):
        return self.__topic
    
    @Model.nodeSetter
    def setTopic(self, topic):
        self.__topic = topic
    
    #Marker: 0..* reference
    #getter, adder, remover
    def getMarkers(self):
        return self.__markers
    
    @Model.nodeAdder
    def addMarker(self, marker):
        self.__markers.append(marker)
    
    @Model.nodeRemover
    def removeMarker(self, marker):
        self.__markers.remove(marker)