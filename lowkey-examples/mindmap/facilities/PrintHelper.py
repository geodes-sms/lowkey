import os
import sys

from lowkey.collabtypes.Model import Model
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.Marker import Marker
from metamodel.entities.MindMap import MindMap
from metamodel.entities.SubTopic import SubTopic
from metamodel.entities.Topic import Topic

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")



def printMindmap(mindmapClabject):
    mindmap = MindMap(clabject=mindmapClabject)
    print("\nPrinting Mindmap {}".format(mindmap.getTitle()))
    print('===============================')
    centralTopicClabject = mindmap.getTopic()
    if(centralTopicClabject):
        centralTopic = CentralTopic(clabject=centralTopicClabject)
        __printTopic(0, centralTopic)
        mainTopicClabjects = centralTopic.getMainTopics()
        if(mainTopicClabjects):
            for mainTopicClabject in mainTopicClabjects:
                mainTopic = MainTopic(mainTopicClabject)
                __printTopic(1, mainTopic)
                subTopicClabjects = mainTopic.getSubTopics()
                if(subTopicClabjects):
                    for subTopicClabject in subTopicClabjects:
                        subTopic = SubTopic(subTopicClabject)
                        __printTopic(2, subTopic)

    
def __printTopic(depth, topic:Topic):
    line = depth * 2 * ' ' + '|_{}'.format(topic.getName())
    markerClabject = topic.getMarker()
    if markerClabject:
        marker = Marker(markerClabject)
        line += (' [' + marker.getSymbol() + ']')
    print(line)

        
def printModel(model: Model):
    print("\nPrinting the nodes of Mindmap model {}".format(model.getTitle()))
    print('===============================')
    for n in model.getNodes():
        print('-"{0}" of type {1}. (ID: {2})'.format(n.getName(), n.__class__.__name__, n.getId()))
