from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Entity import Entity
from lowkey.collabtypes.Model import Model
from metamodel import MindMapPackage

from .CentralTopic import CentralTopic


class MindMap(Entity):
    
    def __init__(self, clabject:Clabject=None):
        if not clabject:
            clabject = Clabject()
            clabject.setType(MindMapPackage.TYPE_MINDMAP)
        super().__init__(clabject)

    # title: Attribute
    # ========================
    # Multiplicity: 1
    # Type: String
    # ========================
    # Methods: get, set
    def getTitle(self):
        return self.getAttribute(MindMapPackage.TITLE)

    def setTitle(self, title):
        self.setAttribute(MindMapPackage.TITLE, title)
    
    # topic: Reference
    # ========================
    # Type: CentralTopic
    # MultiplicityFrom: 1..1
    # MultiplicityTo: 1..1
    # IsComposition: True
    # ========================
    # Methods: get, set, remove
    def getTopic(self):
        model = self.getModel()
        if not model:
            return None
        
        topicAssociations = [a for a in model.getAssociationsByName(MindMapPackage.ASSOCIATION_MINDMAP_CENTRALTOPIC) if a.getFrom() == self._clabject]
        
        if topicAssociations:
            return topicAssociations[0].getTo()  # safe due to MultiplicityToMax = 1
        return None
    
    def setTopic(self, topic: CentralTopic):  # typing due to Type: CentralTopic
        model = self.getModel()
        if not model:
            return None
        
        topicAssociations = [a for a in model.getAssociationsByName(MindMapPackage.ASSOCIATION_MINDMAP_CENTRALTOPIC) if a.getFrom() == self._clabject]
        
        if topicAssociations:
            # Removes the association to the Marker object but not the object
            # safe due to MultiplicityToMax = 1
            model.removeNode(topicAssociations[0])
        
        topicAssociation = Association()
        topicAssociation.setName(MindMapPackage.ASSOCIATION_MINDMAP_CENTRALTOPIC)
        topicAssociation.setFrom(self)
        topicAssociation.setTo(topic)
        topicAssociation.setComposition(True)
        
        model.addNode(topicAssociation)
    
    def removeTopic(self):
        model = self.getModel()
        if not model:
            return None
        
        topicAssociations = [a for a in model.getAssociationsByName(MindMapPackage.ASSOCIATION_MINDMAP_CENTRALTOPIC) if a.getFrom() == self._clabject]

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
        model = self.getModel()
        if not model:
            return None
        
        markerAssociations = [a for a in self.getModel().getAssociationsByName(MindMapPackage.ASSOCIATION_MINDMAP_MARKER) if a.getFrom() == self._clabject]
        
        markers = []
        for a in markersAssociations:
            markers.append(a.getTo())
        return markers
    
    def addMarker(self, marker):
        markersAssociation = Association()
        markersAssociation.setName(MindMapPackage.ASSOCIATION_MARKER)
        markersAssociation.setFrom(self)
        markersAssociation.setTo(marker)
        markersAssociation.setComposition(True)
        
        self.getModel().addNode(markersAssociation)
        
    def removeMarker(self, marker):  # Removes the association to the Marker object but not the object
        model = self.getModel()
        if not model:
            return None
        
        markersAssociations = [a for a in model.getAssociationsByName(MindMapPackage.ASSOCIATION_MINDMAP_MARKER) if a.getFrom() == self._clabject]
            
        for a in markersAssociations:
            if a.getTo() == marker:
                model.removeNode(a)
                return
