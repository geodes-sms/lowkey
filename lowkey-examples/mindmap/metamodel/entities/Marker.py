from collabtypes.Entity import Entity

class Marker(Entity):
    
    def __init__(self, symbol=""):
        super().__init__()
        self.setSymbol(symbol)

    def getSymbol(self):
        return self._getAttribute("symbol")
        
    def setSymbol(self, symbol):
        self._setAttribute("symbol", symbol)