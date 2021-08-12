from editor import MindMapPackage

from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clabject import Clabject

from .Topic import Topic


class SubTopicLiterals():
    ASSOCIATION_SUBTOPICS = "subtopics"


class SubTopic(Topic):
    
    def __init__(self, clabject:Clabject=None):
        if not clabject:
            clabject = Clabject()
            clabject.setType(MindMapPackage.TYPE_SUBTOPIC)
        super().__init__(clabject)
        
    # subTopics: Reference
    # ========================
    # Type: SubTopic
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 1..*
    # IsComposition: True
    # ========================
    # Methods: get, set, remove
    def getSubTopics(self):
        subTopicsAssociations = [a for a in self.getModel().getAssociationsByName(SubTopicLiterals.ASSOCIATION_SUBTOPICS) if a.getFrom() == self._clabject]
        
        subTopics = []
        for a in subTopicsAssociations:
            subTopics.append(a.getTo())
        return subTopics
    
    def addSubTopic(self, subTopic):
        subTopicAssociation = Association()
        subTopicAssociation.setName(SubTopicLiterals.ASSOCIATION_SUBTOPICS)
        subTopicAssociation.setFrom(self)
        subTopicAssociation.setTo(subTopic)
        subTopicAssociation.setComposition(True)
        
        self.getModel().addNode(subTopicAssociation)
        
    def removeSubTopic(self, subTopic):
        model = self.getModel()
        subTopicAssociations = [a for a in model.getAssociationsByName(SubTopicLiterals.ASSOCIATION_SUBTOPICS) if a.getFrom() == self._clabject]

        for a in subTopicAssociations:
            if a.getTo() == subTopic:
                model.removeNode(a)
                return

