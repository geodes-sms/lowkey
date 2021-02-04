from mindmap.metamodel.entities.MindMap import MindMap
from mindmap.metamodel.entities.CentralTopic import CentralTopic
from mindmap import MindmapPrinter

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