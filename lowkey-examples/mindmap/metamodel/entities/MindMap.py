import time

from collabtypes.Entity import Entity
from collabtypes.Relationship import Relationship

from mindmap.metamodel.entities.CentralTopic import CentralTopic


def halt():
    time.sleep(0.001)


class MindMap(Entity):
    
    def __init__(self, title=""):
        super().__init__()
        self.setTitle(title)
        self._topic = None
        # self._markers = []

    # Title: attribute
    # getter, setter
    def getTitle(self):
        return self._getAttribute("title")

    def setTitle(self, title):
        self._setAttribute("title", title)
    
    # Topic: 0..1 reference
    # getter, setter
    def getTopic(self) -> CentralTopic:
        topic = self._getRelationship("topic")
        if topic:
            return topic[0].getTo()
        return None
    
    def setTopic(self, topic):
        if self.getTopic():
            self.remove("topic", self._currentTime())
            halt()
        
        mindMapTopic = Relationship()
        mindMapTopic._setName("topic")
        mindMapTopic.setFrom(self)
        mindMapTopic.setTo(topic)
        mindMapTopic.setAggregation(True)
        
        self._addRelationship(mindMapTopic)
    
    """
    # Marker: 0..* reference
    # getter, adder, remover
    def getMarkers(self):
        return self.__markers
    
    def addMarker(self, marker):
        super()._addNode(marker)
        self.__markers.append(marker)
    
    def removeMarker(self, marker):
        super()._removeNode(marker)
        self.__markers.remove(marker)
    """
