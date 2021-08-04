from lowkey.collabtypes.Association import Association

from .Topic import Topic


class CentralTopicLiterals():
    ASSOCIATION_MAINTOPICS = "maintopic"


class CentralTopic(Topic):
    
    def __init__(self, name=""):
        super().__init__(name)
    
    # mainTopics: Reference
    # ========================
    # Type: MainTopic
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 0..*
    # IsComposition: True
    # ========================
    # Methods: get, set, remove
    def getMainTopics(self):
        mainTopicsAssociations = [a for a in self.getModel().getAssociationsByName(CentralTopicLiterals.ASSOCIATION_MAINTOPICS) if a.getFrom() == self]
        
        mainTopics = []
        for a in mainTopicsAssociations:
            mainTopics.append(a.getTo())
        return mainTopics
    
    def addMainTopic(self, mainTopic):
        mainTopicsAssociation = Association()
        mainTopicsAssociation.setName(CentralTopicLiterals.ASSOCIATION_MAINTOPICS)
        mainTopicsAssociation.setFrom(self)
        mainTopicsAssociation.setTo(mainTopic)
        mainTopicsAssociation.setComposition(True)
        
        self.getModel().addNode(mainTopicsAssociation)

    def removeMainTopic(self, mainTopic):
        model = self.getModel()
        mainTopicAssociations = [a for a in model.getAssociationsByName(CentralTopicLiterals.ASSOCIATION_MAINTOPICS) if a.getFrom() == self]

        for a in mainTopicAssociations:
            if a.getTo() == mainTopic:
                model.removeNode(a)
                return
