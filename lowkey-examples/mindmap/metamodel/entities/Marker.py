from collabtypes.Entity import Entity

class Marker(Entity):
    
    def __init__(self, symbol=""):
        super().__init__()
        self.__symbol = symbol

    def getSymbol(self):
        return self.__symbol
        
    def setSymbol(self, symbol):
        self.__symbol = symbol