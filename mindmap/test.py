from metamodel.entities.MindMap import MindMap
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.SubTopic import SubTopic
from metamodel.entities.Marker import Marker


def printMindMap(mindmap):
    print(mindmap.name)
    centralTopic = mindmap.topic
    printTopic(0, centralTopic)
    for mainTopic in centralTopic.mainTopics:
        printTopic(1, mainTopic)
        for subTopic in mainTopic.subTopics:
            printTopic(2, subTopic)
            
def printTopic(depth, topic):
    print(depth*2*' ' + '|_{}'.format(topic.name) + (' [x]' if topic.marker!=None else ''))

mindmap = MindMap('improvePublicationRecord')

c = CentralTopic('publishPaper')
mindmap.topic = c

mt1 = MainTopic('experiment')
c.mainTopics.append(mt1)
mt2 = MainTopic('writePaper')
c.mainTopics.append(mt2)
c.addRelationship()
#c.addMainTopic(mt2)

s1 = SubTopic('relatedWork')
mt2.subTopics.append(s1)
s2 = SubTopic('contributions')
mt2.subTopics.append(s2)

x = Marker('currentStatus')
mindmap.markers.append(x)
s2.marker = x

printMindMap(mindmap)

