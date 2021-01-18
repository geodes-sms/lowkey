from .Topic import Topic

class SubTopic(Topic):
    
    def __init__(self, name):
        super().__init__(name)
        self.subTopics = []