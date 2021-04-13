from collabtypes.Relationship import Relationship

from .Topic import Topic


class CentralTopic(Topic):
    
    def __init__(self, name=""):
        super().__init__(name)
    
    # mainTopics: Reference
    # ========================
    # Type: MainTopic
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 0..*
    # IsAggregation: True
    # ========================
    # Methods: get, set, remove
    def getMainTopics(self):
        mainTopics = []
        relationships = self.getRelationship("maintopics")
        for r in relationships:
            mainTopics.append(r.getTo())
        return mainTopics
    
    def addMainTopic(self, mainTopic):
        mainTopic_ = Relationship()
        mainTopic_.setName("maintopics")
        mainTopic_.setFrom(self)
        mainTopic_.setTo(mainTopic)
        mainTopic_.setAggregation(True)
        
        self.addRelationship(mainTopic_)
        
    def removeMainTopic(self, mainTopic):
        self.removeRelationship(mainTopic)
