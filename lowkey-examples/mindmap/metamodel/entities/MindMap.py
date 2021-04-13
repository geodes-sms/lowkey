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
        topicReferences = self.getRelationship("topic")
        if topicReferences:
            return topicReferences[0].getTo()  # safe due to MultiplicityToMax = 1
        return None
    
    def setTopic(self, topic: CentralTopic):  # typing due to Type: CentralTopic
        topicReferences = self.getRelationship("topic") 
        if topicReferences:
            # Removes the relationship to the Marker object but not the object
            # safe due to MultiplicityToMax = 1
            self.removeRelationship(topicReferences[0])
        
        topicReference = Relationship()
        topicReference.setName("topic")
        topicReference.setFrom(self)
        topicReference.setTo(topic)
        topicReference.setAggregation(True)
        
        self.addRelationship(topicReference)
    
    def removeTopic(self):
        topicReferences = self.getRelationship("topic")
        if topicReferences:
            self.removeRelationship(topicReferences[0]) # safe due to MultiplicityToMax = 1
    
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
        markersReferences = self.getRelationship("markers")
        for r in markersReferences:
            markers.append(r.getTo())
        return markers
    
    def addMarker(self, marker):
        markersReference = Relationship()
        markersReference.setName("markers")
        markersReference.setFrom(self)
        markersReference.setTo(marker)
        markersReference.setAggregation(True)
        
        self.addRelationship(markersReference)
        
    def removeMarker(self, marker): # Removes the relationship to the Marker object but not the object
        markersReferences = self.getRelationship("markers")
        for mr in markersReferences:
            if mr.getTo() == marker:
                self.removeRelationship(mr)
                return