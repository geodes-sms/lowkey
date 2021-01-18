from collabtypes.Entity import Entity

class Topic(Entity):
    
    def __init__(self, name):
        super().__init__(name)
        self.marker = None