from lowkey.collabtypes.Model import Model
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Entity import Entity

from .CentralTopic import CentralTopic
from mindmap.editor import MindMapPackage


class MindMapLiterals():
    TITLE = "title"
    ASSOCIATION_TOPIC = "topic"
    ASSOCIATION_MARKER = "markers"


class MindMap(Entity):
    
    def __init__(self, title="", clabject:Clabject=None):
        if not clabject:
            clabject = Clabject()
            clabject.setType(MindMapPackage.TYPE_MINDMAP)
        super().__init__(clabject)
        self.setName(title)
        self.setTitle(title)

    # title: Attribute
    # ========================
    # Multiplicity: 1
    # Type: String
    # ========================
    # Methods: get, set
    def getTitle(self):
        return self.getAttribute(MindMapLiterals.TITLE)

    def setTitle(self, title):
        self.setAttribute(MindMapLiterals.TITLE, title)
    
    # topic: Reference
    # ========================
    # Type: CentralTopic
    # MultiplicityFrom: 1..1
    # MultiplicityTo: 1..1
    # IsComposition: True
    # ========================
    # Methods: get, set, remove
    def getTopic(self):
        topicAssociations = [a for a in self.getModel().getAssociationsByName(MindMapLiterals.ASSOCIATION_TOPIC) if a.getFrom() == self]
        
        if topicAssociations:
            return topicAssociations[0].getTo()  # safe due to MultiplicityToMax = 1
        return None
    
    def setTopic(self, topic: CentralTopic):  # typing due to Type: CentralTopic
        model = self.getModel()
        topicAssociations = [a for a in model.getAssociationsByName(MindMapLiterals.ASSOCIATION_TOPIC) if a.getFrom() == self]
        
        if topicAssociations:
            # Removes the association to the Marker object but not the object
            # safe due to MultiplicityToMax = 1
            model.removeNode(topicAssociations[0])
        
        topicAssociation = Association()
        topicAssociation.setName(MindMapLiterals.ASSOCIATION_TOPIC)
        topicAssociation.setFrom(self)
        topicAssociation.setTo(topic)
        topicAssociation.setComposition(True)
        
        model.addNode(topicAssociation)
    
    def removeTopic(self):
        model = self.getModel()
        topicAssociations = [a for a in model.getAssociationsByName(MindMapLiterals.ASSOCIATION_TOPIC) if a.getFrom() == self]

        if topicAssociations:
            model.removeNode(topicAssociations[0])  # safe due to MultiplicityToMax = 1
    
    # markers: Reference
    # ========================
    # Type: Marker
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 0..*
    # IsComposition: True
    # ========================
    # Methods: get, add, remove
    def getMarkers(self):
        markerAssociations = [a for a in self.getModel().getAssociationsByName(MindMapLiterals.ASSOCIATION_MARKER) if a.getFrom() == self]
        
        markers = []
        for a in markersAssociations:
            markers.append(a.getTo())
        return markers
    
    def addMarker(self, marker):
        markersAssociation = Association()
        markersAssociation.setName(MindMapLiterals.ASSOCIATION_MARKER)
        markersAssociation.setFrom(self)
        markersAssociation.setTo(marker)
        markersAssociation.setComposition(True)
        
        self.getModel().addNode(markersAssociation)
        
    def removeMarker(self, marker):  # Removes the association to the Marker object but not the object
        model = self.getModel()
        markersAssociations = [a for a in model.getAssociationsByName(MindMapLiterals.ASSOCIATION_MARKER) if a.getFrom() == self]
            
        for a in markersAssociations:
            if a.getTo() == marker:
                model.removeNode(a)
                return
