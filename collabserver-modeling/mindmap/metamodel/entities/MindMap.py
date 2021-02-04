from collabtypes.Model import Model

class MindMap(Model):
    
    def __init__(self, title):
        super().__init__()
        self.__title = title
        self.__topic = None
        self.__markers = []

    #Title: attribute
    #getter, setter
    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        super._setAttribute(title)
        self.__title = title
    
    #Topic: 0..1 reference
    #getter, setter
    def getTopic(self):
        return self.__topic
    
    def setTopic(self, topic):
        super()._setNode(self.__topic, topic)
        self.__topic = topic
    
    #Marker: 0..* reference
    #getter, adder, remover
    def getMarkers(self):
        return self.__markers
    
    def addMarker(self, marker):
        super()._addNode(marker)
        self.__markers.append(marker)
    
    def removeMarker(self, marker):
        super()._removeNode(marker)
        self.__markers.remove(marker)