from mindmap.editor import MindMapPackage

from lowkey.collabtypes.Association import Association
from lowkey.collabtypes.Clabject import Clabject

from .Topic import Topic


class MainTopicLiterals():
    ASSOCIATION_SUBTOPICS = "subtopics"


class MainTopic(Topic):
    
    def __init__(self, name="", clabject:Clabject=None):
        if not clabject:
            clabject = Clabject()
            clabject.setType(MindMapPackage.TYPE_MAIN_TOPIC)
        super().__init__(name, clabject)
        
    # subTopics: Reference
    # ========================
    # Type: SubTopic
    # MultiplicityFrom: 0..1
    # MultiplicityTo: 1..*
    # IsComposition: True
    # ========================
    # Methods: get, set, remove
    def getSubTopics(self):
        subTopicsAssociations = [a for a in self.getModel().getAssociationsByName(MainTopicLiterals.ASSOCIATION_SUBTOPICS) if a.getFrom() == self]
        
        subTopics = []
        for a in subTopicsAssociations:
            subTopics.append(a.getTo())
        return subTopics
    
    def addSubTopic(self, subTopic):
        subTopicAssociation = Association()
        subTopicAssociation.setName(MainTopicLiterals.ASSOCIATION_SUBTOPICS)
        subTopicAssociation.setFrom(self)
        subTopicAssociation.setTo(subTopic)
        subTopicAssociation.setComposition(True)
        
        self.getModel().addNode(subTopicAssociation)
        
    def removeSubTopic(self, subTopic):
        model = self.getModel()
        subTopicAssociations = [a for a in model.getAssociationsByName(MainTopicLiterals.ASSOCIATION_SUBTOPICS) if a.getFrom() == self]

        for a in subTopicAssociations:
            if a.getTo() == subTopic:
                model.removeNode(a)
                return
