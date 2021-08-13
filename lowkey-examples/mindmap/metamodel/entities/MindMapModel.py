from lowkey.collabtypes.Model import Model
from metamodel import MindMapPackage

from .MindMap import MindMap


class MindMapModel(Model):
    
    def __init__(self, title=""):
        super().__init__()
        self.setTitle(title)

    # title: Attribute
    # ========================
    # Multiplicity: 1
    # Type: String
    # ========================
    # Methods: get, set
    def getTitle(self):
        return self.getAttribute(MindMapPackage.TITLE)

    def setTitle(self, title):
        self.setAttribute(MindMapPackage.TITLE, title)
        
    def getMindmaps(self):
        return [c for c in self.getClabjects() if c.getType() == MindMapPackage.TYPES.MINDMAP]
