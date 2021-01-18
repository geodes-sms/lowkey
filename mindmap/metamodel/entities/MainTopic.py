from .Topic import Topic

class MainTopic(Topic):
    
    def __init__(self, name):
        super().__init__(name)
        self.subTopics = []