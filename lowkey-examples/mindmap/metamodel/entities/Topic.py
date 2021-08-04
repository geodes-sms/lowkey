from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Association import Association

from .Marker import Marker


class TopicLiterals():
    ASSOCIATION_MARKER = "marker"


class Topic(Clabject):
    
    def __init__(self, name=""):
        super().__init__()
        self.setName(name)
        
    # marker: Reference
    # ========================
    # Type: Marker
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 0..1
    # IsComposition: False
    # ========================
    # Methods: get, set, remove
    def getMarker(self) -> Marker:
        markerAssociations = [a for a in self.getModel().getAssociationsByName(TopicLiterals.ASSOCIATION_MARKER) if a.getFrom() == self]
        
        if markerAssociations:
            return markerAssociations[0].getTo()  # safe due to MultiplicityToMax = 1
        return None
    
    def setMarker(self, marker: Marker):  # typing due to Type: Marker
        model = self.getModel()
        markerAssociations = [a for a in model.getAssociationsByName(TopicLiterals.ASSOCIATION_MARKER) if a.getFrom() == self]
        
        if markerAssociations:
            # Removes the association to the Marker object but not the object
            # safe due to MultiplicityToMax = 1
            model.removeNode(markerAssociations[0])
        
        markerAssociation = Association()
        markerAssociation.setName(TopicLiterals.ASSOCIATION_MARKER)
        markerAssociation.setFrom(self)
        markerAssociation.setTo(marker)
        markerAssociation.setComposition(True)
        
        model.addNode(markerAssociation)
        
    def removeMarker(self):  # Removes the association to the Marker object but not the object
        model = self.getModel()
        markerAssociations = [a for a in model.getAssociationsByName(TopicLiterals.ASSOCIATION_MARKER) if a.getFrom() == self]

        for a in markerAssociations:
            model.removeNode(markerAssociations[0])  # safe due to MultiplicityToMax = 1
