from collabtypes.Relationship import Relationship

class CentralTopic_MainTopic_mainTopics(Relationship):
    
    def __init__(self, name):
        super().__init__('mainTopics')
        