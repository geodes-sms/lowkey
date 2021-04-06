from collabtypes.Entity import Entity

class Topic(Entity):
    
    def __init__(self, name=""):
        super().__init__()
        self._setName(name)
        #self.__marker = None
        
    def getName(self):
        return self._getAttribute("name")
        
    def setName(self, name):
        self._setAttribute("name", name)

    #def getMarker(self):
    #    return self.__marker

    #def setMarker(self, marker):
    #    self.__marker = marker