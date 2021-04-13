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
        mainTopicsReferences = self.getRelationship("maintopics")
        for r in mainTopicsReferences:
            mainTopics.append(r.getTo())
        return mainTopics
    
    def addMainTopic(self, mainTopic):
        mainTopicsReference = Relationship()
        mainTopicsReference.setName("maintopics")
        mainTopicsReference.setFrom(self)
        mainTopicsReference.setTo(mainTopic)
        mainTopicsReference.setAggregation(True)
        
        self.addRelationship(mainTopicsReference)
        
    def removeMainTopic(self, mainTopic):
        self.removeRelationship(mainTopic)
