from lowkey.collabtypes.Model import Model


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
        return self.getAttribute("title")

    def setTitle(self, title):
        self.setAttribute("title", title)
