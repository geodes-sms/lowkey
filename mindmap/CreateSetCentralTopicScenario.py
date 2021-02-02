from metamodel.entities.MindMap import MindMap
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.SubTopic import SubTopic
from metamodel.entities.Marker import Marker
import MindmapPrinter

#Create MindMap
mindmap = MindMap('improvePublicationRecord')

#Create CentralTopic and add to the MindMap
c = CentralTopic('publishPaper')
mindmap.setTopic(c)

#Print the MindMap
MindmapPrinter.printMindmap(mindmap)
MindmapPrinter.printNodes(mindmap)

#Create CentralTopic and add to the MindMap
c2 = CentralTopic('goToVacation')
mindmap.setTopic(c2)

#Print the MindMap
MindmapPrinter.printMindmap(mindmap)
MindmapPrinter.printNodes(mindmap)