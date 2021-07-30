from lowkey.collabtypes.Entity import Entity
from lowkey.collabtypes.Relationship import Relationship

from .Marker import Marker


class Topic(Entity):
    
    def __init__(self, name=""):
        super().__init__()
        self.setName(name)
        
    # marker: Reference
    # ========================
    # Type: Marker
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 0..1
    # IsAggregation: False
    # ========================
    # Methods: get, set, remove
    def getMarker(self) -> Marker:
        markerReference = self.getRelationship("marker")
        if markerReference:
            return markerReference[0].getTo()  # safe due to MultiplicityToMax = 1
        return None
    
    def setMarker(self, marker: Marker):  # typing due to Type: Marker
        if self.getMarker():  # required due to MultiplicityToMax = 1
            self.removeMarker()
        
        markerReference = Relationship()
        markerReference.setName("marker")
        markerReference.setFrom(self)
        markerReference.setTo(marker)
        markerReference.setAggregation(True)
        
        self.addRelationship(markerReference)
        
    def removeMarker(self):  # Removes the relationship to the Marker object but not the object
        markerReference = self.getRelationship("marker")
        if markerReference:
            self.removeRelationship(markerReference[0])  # safe due to MultiplicityToMax = 1
