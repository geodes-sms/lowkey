from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Entity import Entity

from metamodel import MindMapPackage

from .Marker import Marker


class Topic(Entity):
    
    def __init__(self, clabject:Clabject=None):
        assert clabject
        super().__init__(clabject)
        
    def update(self):
        self.getPersistence()
        
    # marker: Reference
    # ========================
    # Type: Marker
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 0..1
    # IsComposition: False
    # ========================
    # Methods: get, set, remove
    def getMarker(self):
        markerAssociations = [a for a in self.getModel().getAssociationsByName(MindMapPackage.ASSOCIATION_TOPIC_MARKER) if a.getFrom() == self._clabject]
        
        if markerAssociations:
            return markerAssociations[0].getTo()  # safe due to MultiplicityToMax = 1
        return None
    
    def setMarker(self, marker: Marker):  # typing due to Type: Marker
        model = self.getModel()
        markerAssociations = [a for a in model.getAssociationsByName(MindMapPackage.ASSOCIATION_TOPIC_MARKER) if a.getFrom() == self._clabject]
        
        if markerAssociations:
            # Removes the association to the Marker object but not the object
            # safe due to MultiplicityToMax = 1
            model.removeNode(markerAssociations[0])
        
        markerAssociation = Association()
        markerAssociation.setName(MindMapPackage.ASSOCIATION_TOPIC_MARKER)
        markerAssociation.setFrom(self)
        markerAssociation.setTo(marker)
        markerAssociation.setComposition(True)
        
        model.addNode(markerAssociation)
        
    def removeMarker(self):  # Removes the association to the Marker object but not the object
        model = self.getModel()
        markerAssociations = [a for a in model.getAssociationsByName(MindMapPackage.ASSOCIATION_TOPIC_MARKER) if a.getFrom() == self._clabject]

        for a in markerAssociations:
            model.removeNode(markerAssociations[0])  # safe due to MultiplicityToMax = 1
