from collabtypes.Entity import Entity

class Topic(Entity):
    
    def __init__(self, name=""):
        super().__init__()
        self._setName(name)
        self.__marker = None
        
    def getName(self):
        return self._getName()
        
    def setName(self, name):
        self._setName(name)

    def getMarker(self):
        return self.__marker

    def setMarker(self, marker):
        self.__marker = marker