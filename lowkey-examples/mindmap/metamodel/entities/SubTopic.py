from lowkey.collabtypes.Association import Association

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
        associations = self.getAssociation("subtopics")
        for a in associations:
            subTopics.append(a.getTo())
        return subTopics
    
    def addSubTopic(self, subTopic):
        subTopic_ = Association()
        subTopic_._setName("subtopics")
        subTopic_.setFrom(self)
        subTopic_.setTo(subTopic)
        subTopic_.setAggregation(True)
        
        self.addAssociation(subTopic_)
        
    def removeSubTopic(self, subTopic):
        self.removeAssociation(subTopic)
