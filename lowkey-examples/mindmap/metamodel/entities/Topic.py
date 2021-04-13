from collabtypes.Entity import Entity
from collabtypes.Relationship import Relationship

from mindmap.metamodel.entities.Marker import Marker


class Topic(Entity):
    
    def __init__(self, name=""):
        super().__init__()
        self.setName(name)

    # name: Attribute
    # ========================
    # Multiplicity: 1
    # Type: String
    # ========================
    # Methods: get, set
    def getName(self):
        return self.getAttribute("name")

    def setName(self, name):
        self.setAttribute("name", name)
        
    # marker: Reference
    # ========================
    # Type: Marker
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 0..1
    # IsAggregation: False
    # ========================
    # Methods: get, set
    def getMarker(self) -> Marker:
        marker = self.getRelationship("marker")
        if marker:
            return marker[0].getTo()  # safe due to MultiplicityToMax = 1
        return None
    
    def setMarker(self, marker: Marker):  # typing due to Type: Marker
        if self.getMarker():  # required due to MultiplicityToMax = 1
            self.remove("marker", self.currentTime())
        
        marker_ = Relationship()
        marker_.setName("marker")
        marker_.setFrom(self)
        marker_.setTo(marker)
        marker_.setAggregation(True)
        
        self.addRelationship(marker_)
