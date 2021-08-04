from lowkey.collabtypes.Model import Model
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Entity import Entity
from lowkey.collabtypes.Association import Association

from .CentralTopic import CentralTopic


class MindMap(Entity):
    
    def __init__(self, title=""):
        super().__init__()
        self.setTitle(title)
        self.setName(title+"_mindmap")

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
        topicAssociations = self.getAssociationsByName("topic")
        if topicAssociations:
            return topicAssociations[0].getTo()  # safe due to MultiplicityToMax = 1
        return None
    
    def setTopic(self, topic: CentralTopic):  # typing due to Type: CentralTopic
        topicReferences = self.getAssociationsByName("topic") 
        if topicReferences:
            # Removes the association to the Marker object but not the object
            # safe due to MultiplicityToMax = 1
            self.removeAssociation(topicReferences[0])
        
        topicAssociation = Association()
        topicAssociation.setName("topic")
        topicAssociation.setFrom(self)
        topicAssociation.setTo(topic)
        topicAssociation.setAggregation(True)
        
        self.addAssociation(topicAssociation)
    
    def removeTopic(self):
        topicAssociations = self.getAssociationsByName("topic")
        if topicAssociations:
            self.removeAssociation(topicAssociations[0])  # safe due to MultiplicityToMax = 1
    
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
        markersAssociations = self.getAssociationsByName("markers")
        for a in markersAssociations:
            markers.append(a.getTo())
        return markers
    
    def addMarker(self, marker):
        markersAssociation = Association()
        markersAssociation.setName("markers")
        markersAssociation.setFrom(self)
        markersAssociation.setTo(marker)
        markersAssociation.setAggregation(True)
        
        self.addAssociation(markersAssociation)
        
    def removeMarker(self, marker):  # Removes the association to the Marker object but not the object
        markersAssociations = self.getAssociationsByName("markers")
        for a in markersAssociations:
            if a.getTo() == marker:
                self.removeAssociation(a)
                return
