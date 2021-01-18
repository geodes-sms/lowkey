from collabtypes.Model import Model

class MindMap(Model):
    
    def __init__(self, name):
        super().__init__(name)
        self.markers = []