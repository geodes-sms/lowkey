from lowkey.collabtypes.Model import Model


def printMindmap(mindmap):
    print("\nPrinting Mindmap {}".format(mindmap.getTitle()))
    print('===============================')
    centralTopic = mindmap.getTopic()
    if(centralTopic):
        __printTopic(0, centralTopic)
        mainTopics = centralTopic.getMainTopics()
        if(mainTopics):
            for mainTopic in mainTopics:
                __printTopic(1, mainTopic)
                subTopics = mainTopic.getSubTopics()
                if(subTopics):
                    for subTopic in mainTopic.getSubTopics():
                        __printTopic(2, subTopic)

    
def __printTopic(depth, topic):
    line = depth * 2 * ' ' + '|_{}'.format(topic.getName())
    marker = topic.getMarker()
    if marker:
        line += (' [' + marker.getSymbol() + ']')
    print(line)

        
def printModel(model: Model):
    print("\nPrinting the nodes of Mindmap model {}".format(model.getTitle()))
    print('===============================')
    for n in model.getNodes():
        print('-"{0}" of type {1}. (ID: {2})'.format(n.getName(), n.__class__.__name__, n.getId()))
