from .Topic import Topic

class SubTopic(Topic):
    
    def __init__(self, name=""):
        super().__init__(name)
        self.__subTopics = []
    
    def getSubTopics(self):
        return self.__subTopics
        
    def addSubTopic(self, subTopic):
        self.__subTopics.append(subTopic)