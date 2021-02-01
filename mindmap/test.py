from metamodel.entities.MindMap import MindMap
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.SubTopic import SubTopic
from metamodel.entities.Marker import Marker


def printMindMap(mindmap):
    print(mindmap.getTitle())
    centralTopic = mindmap.getTopic()
    printTopic(0, centralTopic)
    for mainTopic in centralTopic.getMainTopics():
        printTopic(1, mainTopic)
        for subTopic in mainTopic.getSubTopics():
            printTopic(2, subTopic)
            
def printTopic(depth, topic):
    line = depth*2*' ' + '|_{}'.format(topic.getName())
    marker = topic.getMarker()
    if(marker !=None):
        line+=(' [' + marker.getSymbol() + ']')
    print(line)

    
#Create MindMap
mindmap = MindMap('improvePublicationRecord')

#Create CentralTopic and add to the MindMap
c = CentralTopic('publishPaper')
mindmap.setTopic(c)

#Create two MainTopics and add them to the CentralTopic
mt1 = MainTopic('experiment')
c.addMainTopic(mt1)
##Create this one with a missing argument
mt2 = MainTopic()
mt2.setName('writePaper')
c.addMainTopic(mt2)

#Create two SubTopics and add them to one of the MainTopics
s1 = SubTopic('relatedWork')
mt2.addSubTopic(s1)
s2 = SubTopic('contributions')
mt2.addSubTopic(s2)

#Create a Marker
x = Marker('x')
mindmap.addMarker(x)
s2.setMarker(x)


#Print the MindMap
printMindMap(mindmap)