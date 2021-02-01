from collabtypes.Model import Model

class MindMap(Model):
    
    def __init__(self, title):
        super().__init__()
        self.__title = title
        self.__topic = None
        self.__markers = []

    def getTitle(self):
        return self.__title
        
    def setTitle(self, title):
        self.__title = title
        
    def getTopic(self):
        return self.__topic
        
    def setTopic(self, topic):
        self.__topic = topic
    
    def getMarkers(self):
        return self.__markers
    
    def addMarker(self, marker):
        self.__markers.append(marker)