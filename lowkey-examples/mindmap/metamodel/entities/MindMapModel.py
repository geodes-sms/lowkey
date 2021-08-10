from lowkey.collabtypes.Model import Model

from .MindMap import MindMap


class MindMapModelLiterals():
    TITLE = "title"


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
        return self.getAttribute(MindMapModelLiterals.TITLE)

    def setTitle(self, title):
        self.setAttribute(MindMapModelLiterals.TITLE, title)
        
    def getMindmaps(self):
        return [c for c in self.getClabjects() if isinstance(c, MindMap)]
