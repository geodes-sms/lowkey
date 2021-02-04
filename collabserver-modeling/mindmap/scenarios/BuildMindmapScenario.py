from mindmap.metamodel.entities.MindMap import MindMap
from mindmap.metamodel.entities.CentralTopic import CentralTopic
from mindmap.metamodel.entities.MainTopic import MainTopic
from mindmap.metamodel.entities.SubTopic import SubTopic
from mindmap.metamodel.entities.Marker import Marker
from mindmap import MindmapPrinter

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
MindmapPrinter.printMindmap(mindmap)