from collabtypes.Model import Model


def printMindmap(mindmap):
    print("\nPrinting Mindmap")
    print('===============================')
    print(mindmap.getTitle())
    centralTopic = mindmap.getTopic()
    __printTopic(0, centralTopic)
    for mainTopic in centralTopic.getMainTopics():
        __printTopic(1, mainTopic)
        for subTopic in mainTopic.getSubTopics():
            __printTopic(2, subTopic)

    
def __printTopic(depth, topic):
    line = depth * 2 * ' ' + '|_{}'.format(topic.getName())
    marker = topic.getMarker()
    if marker:
        line += (' [' + marker.getSymbol() + ']')
    print(line)

        
def printModel(model: Model):
    print("\nPrinting model nodes")
    print('===============================')
    for n in model.getNodes():
        print('-"{0}" of type {1}. (ID: {2})'.format(n.getName(), n.__class__.__name__, n.getId()))
