from collabtypes.Entity import Entity

class Topic(Entity):
    
    def __init__(self, name=""):
        super().__init__()
        self.__name = name
        self.__marker = None
        
    def getName(self):
        return self.__name
        
    def setName(self, name):
        self.__name = name

    def getMarker(self):
        return self.__marker

    def setMarker(self, marker):
        self.__marker = marker