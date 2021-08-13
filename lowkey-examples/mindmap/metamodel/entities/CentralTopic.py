from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clabject import Clabject
from metamodel import MindMapPackage

from .Topic import Topic


class CentralTopic(Topic):
    
    def __init__(self, clabject:Clabject=None):
        if not clabject:
            clabject = Clabject()
            clabject.setType(MindMapPackage.TYPE_CENTRAL_TOPIC)
        super().__init__(clabject)
    
    # mainTopics: Reference
    # ========================
    # Type: MainTopic
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 0..*
    # IsComposition: True
    # ========================
    # Methods: get, set, remove
    def getMainTopics(self):
        mainTopicsAssociations = [a for a in self.getModel().getAssociationsByName(MindMapPackage.ASSOCIATION_CENTRALTOPIC_MAINTOPIC) if a.getFrom() == self._clabject]
        
        mainTopics = []
        for a in mainTopicsAssociations:
            mainTopics.append(a.getTo())
        return mainTopics
    
    def addMainTopic(self, mainTopic):
        mainTopicsAssociation = Association()
        mainTopicsAssociation.setName(MindMapPackage.ASSOCIATION_CENTRALTOPIC_MAINTOPIC)
        mainTopicsAssociation.setFrom(self)
        mainTopicsAssociation.setTo(mainTopic)
        mainTopicsAssociation.setComposition(True)
        
        self.getModel().addNode(mainTopicsAssociation)

    def removeMainTopic(self, mainTopic):
        model = self.getModel()
        mainTopicAssociations = [a for a in model.getAssociationsByName(MindMapPackage.ASSOCIATION_CENTRALTOPIC_MAINTOPIC) if a.getFrom() == self._clabject]

        for a in mainTopicAssociations:
            if a.getTo() == mainTopic:
                model.removeNode(a)
                return
