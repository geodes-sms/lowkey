from lowkey.collabtypes.Clabject import Clabject


class Marker(Clabject):
    
    def __init__(self, symbol=""):
        super().__init__()
        self.setSymbol(symbol)
        self.setName(symbol+"_marker")
        
    # symbol: Attribute
    # ========================
    # Multiplicity: 1
    # Type: String
    # ========================
    # Methods: get, set
    def getSymbol(self):
        return self.getAttribute("symbol")

    def setSymbol(self, symbol):
        self.setAttribute("symbol", symbol)
