from lowkey.collabtypes.Association import Association

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
        mainTopicsAssociations = self.getAssociationsByName("maintopics")
        for a in mainTopicsAssociations:
            mainTopics.append(a.getTo())
        return mainTopics
    
    def addMainTopic(self, mainTopic):
        mainTopicsAssociation = Association()
        mainTopicsAssociation.setName("maintopics")
        mainTopicsAssociation.setFrom(self)
        mainTopicsAssociation.setTo(mainTopic)
        mainTopicsAssociation.setAggregation(True)
        
        self.addAssociation(mainTopicsAssociation)
        
    def removeMainTopic(self, mainTopic):
        self.removeAssociation(mainTopic)
