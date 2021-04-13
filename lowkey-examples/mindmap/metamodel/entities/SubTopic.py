from collabtypes.Relationship import Relationship

from .Topic import Topic


class SubTopic(Topic):
    
    def __init__(self, name=""):
        super().__init__(name)
    
    # subTopics: Reference
    # ========================
    # Type: SubTopic
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 1..*
    # IsAggregation: True
    # ========================
    # Methods: get, set, remove
    def getSubTopics(self):
        subTopics = []
        relationships = self.getRelationship("subtopics")
        for r in relationships:
            subTopics.append(r.getTo())
        return subTopics
    
    def addSubTopic(self, subTopic):
        subTopic_ = Relationship()
        subTopic_._setName("subtopics")
        subTopic_.setFrom(self)
        subTopic_.setTo(subTopic)
        subTopic_.setAggregation(True)
        
        self.addRelationship(subTopic_)
        
    def removeSubTopic(self, subTopic):
        self.removeRelationship(subTopic)
