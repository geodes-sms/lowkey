from .Topic import Topic
#from ..relationships.CentralTopic_MainTopic_mainTopics import CentralTopic_MainTopic_mainTopics

class CentralTopic(Topic):
    
    def __init__(self, name):
        super().__init__(name)
        self.mainTopics = []
        
#    def addMainTopic(self, mainTopic):
#        super().addRelationship()