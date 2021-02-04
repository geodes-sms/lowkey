def printMindmap(mindmap):
    print('===============================')
    print(mindmap.getTitle())
    centralTopic = mindmap.getTopic()
    __printTopic(0, centralTopic)
    for mainTopic in centralTopic.getMainTopics():
        __printTopic(1, mainTopic)
        for subTopic in mainTopic.getSubTopics():
            __printTopic(2, subTopic)

    
def __printTopic(depth, topic):
    line = depth*2*' ' + '|_{}'.format(topic.getName())
    marker = topic.getMarker()
    if(marker !=None):
        line+=(' [' + marker.getSymbol() + ']')
    print(line)
    
def printNodes(mindmap):
    print('\n')
    for node in mindmap._getNodes():
        print(node)