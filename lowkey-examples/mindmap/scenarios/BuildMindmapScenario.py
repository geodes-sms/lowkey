from mindmap.metamodel.entities.MindMap import MindMap
from mindmap.metamodel.entities.CentralTopic import CentralTopic
from mindmap.metamodel.entities.MainTopic import MainTopic
from mindmap.metamodel.entities.SubTopic import SubTopic
from mindmap.metamodel.entities.Marker import Marker
from mindmap import MindmapPrinter
import time

def halt():
    time.sleep(0.001)

#Create MindMap
mindmap = MindMap('improvePublicationRecord')
halt()

#Create CentralTopic and add to the MindMap
c = CentralTopic('publishPaper')
mindmap.setTopic(c)
halt()

#Create two MainTopics and add them to the CentralTopic
mt1 = MainTopic('experiment')
c.addMainTopic(mt1)
halt()

##Create this one with a missing argument
mt2 = MainTopic()
mt2.setName('writePaper')
halt()
c.addMainTopic(mt2)
halt()

#Create two SubTopics and add them to one of the MainTopics
s1 = SubTopic('relatedWork')
mt2.addSubTopic(s1)
halt()
s2 = SubTopic('contributions')
mt2.addSubTopic(s2)
halt()

#Create a Marker
x = Marker('x')
mindmap.addMarker(x)
halt()
s2.setMarker(x)
halt()

#Print the MindMap
MindmapPrinter.printMindmap(mindmap)