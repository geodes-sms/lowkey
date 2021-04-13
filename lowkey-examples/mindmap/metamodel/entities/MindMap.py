from collabtypes.Entity import Entity
from collabtypes.Relationship import Relationship

from mindmap.metamodel.entities.CentralTopic import CentralTopic


class MindMap(Entity):
    
    def __init__(self, title=""):
        super().__init__()
        self.setTitle(title)

    # title: Attribute
    # ========================
    # Multiplicity: 1
    # Type: String
    # ========================
    # Methods: get, set
    def getTitle(self):
        return self.getAttribute("title")

    def setTitle(self, title):
        self.setAttribute("title", title)
    
    # topic: Reference
    # ========================
    # Type: CentralTopic
    # MultiplicityFrom: 1..1
    # MultiplicityTo: 1..1
    # IsAggregation: True
    # ========================
    # Methods: get, set, remove
    def getTopic(self) -> CentralTopic:
        topic = self.getRelationship("topic")
        if topic:
            return topic[0].getTo()  # safe due to MultiplicityToMax = 1
        return None
    
    def setTopic(self, topic: CentralTopic):  # typing due to Type:O CentralTopic
        if self.getTopic():  # required due to MultiplicityToMax = 1
            self.remove("topic", self.currentTime())
        
        topic_ = Relationship()
        topic_.setName("topic")
        topic_.setFrom(self)
        topic_.setTo(topic)
        topic_.setAggregation(True)
        
        self.addRelationship(topic_)
    
    # markers: Reference
    # ========================
    # Type: Marker
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 0..*
    # IsAggregation: True
    # ========================
    # Methods: get, add, remove
    def getMarkers(self):
        markers = []
        relationships = self.getRelationship("markers")
        for r in relationships:
            markers.append(r.getTo())
        return markers
    
    def addMarker(self, marker):
        marker_ = Relationship()
        marker_.setName("markers")
        marker_.setFrom(self)
        marker_.setTo(marker)
        marker_.setAggregation(True)
        
        self.addRelationship(marker_)
        
    def removeMarker(self, marker):
        self.removeRelationship(marker)

