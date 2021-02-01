from .Topic import Topic

class MainTopic(Topic):
    
    def __init__(self, name=""):
        super().__init__(name)
        self.__subTopics = []
    
    def getSubTopics(self):
        return self.__subTopics
        
    def addSubTopic(self, subTopic):
        self.__subTopics.append(subTopic)