from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Entity import Entity
from metamodel import MindMapPackage


class Marker(Entity):
    
    def __init__(self, clabject:Clabject=None):
        if not clabject:
            clabject = Clabject()
            clabject.setType(MindMapPackage.TYPE_MARKER)
        super().__init__(clabject)
        
    # symbol: Attribute
    # ========================
    # Multiplicity: 1
    # Type: String
    # ========================
    # Methods: get, set
    def getSymbol(self):
        return self.getAttribute(MindMapPackage.MARKER_SYMBOL)

    def setSymbol(self, symbol):
        self.setAttribute(MindMapPackage.MARKER_SYMBOL, symbol)
