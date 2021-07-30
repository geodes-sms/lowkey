from lowkey.collabtypes.Entity import Entity
from lowkey.collabtypes.Association import Association

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
        markerReference = self.getAssociation("marker")
        if markerReference:
            return markerReference[0].getTo()  # safe due to MultiplicityToMax = 1
        return None
    
    def setMarker(self, marker: Marker):  # typing due to Type: Marker
        if self.getMarker():  # required due to MultiplicityToMax = 1
            self.removeMarker()
        
        markerReference = Association()
        markerReference.setName("marker")
        markerReference.setFrom(self)
        markerReference.setTo(marker)
        markerReference.setAggregation(True)
        
        self.addAssociation(markerReference)
        
    def removeMarker(self):  # Removes the association to the Marker object but not the object
        markerReference = self.getAssociation("marker")
        if markerReference:
            self.removeAssociation(markerReference[0])  # safe due to MultiplicityToMax = 1
