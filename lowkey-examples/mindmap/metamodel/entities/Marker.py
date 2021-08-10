from mindmap.editor import MindMapPackage

from lowkey.collabtypes.Clabject import Clabject
from lowkey.collabtypes.Entity import Entity


class MarkerLiterals():
    SYMBOL = "symbol"


class Marker(Entity):
    
    def __init__(self, symbol="", clabject:Clabject=None):
        if not clabject:
            clabject = Clabject()
            clabject.setType(MindMapPackage.TYPE_MARKER)
        super().__init__(clabject)
        self.setSymbol(symbol)
        self.setName(symbol+"_marker")
        
    # symbol: Attribute
    # ========================
    # Multiplicity: 1
    # Type: String
    # ========================
    # Methods: get, set
    def getSymbol(self):
        return self.getAttribute(MarkerLiterals.SYMBOL)

    def setSymbol(self, symbol):
        self.setAttribute(MarkerLiterals.SYMBOL, symbol)
