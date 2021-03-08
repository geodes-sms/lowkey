from mindmap.metamodel.entities.MindMap import MindMap
from mindmap.metamodel.entities.CentralTopic import CentralTopic
from mindmap.metamodel.entities.Marker import Marker
from mindmap import MindmapPrinter

#Create MindMap
mindmap = MindMap('improvePublicationRecord')

#Create CentralTopic and add to the MindMap
c = CentralTopic('publishPaper')
mindmap.setTopic(c)

#Create a Marker
x = Marker('x')
mindmap.addMarker(x)
c.setMarker(x)

#Print the MindMap
MindmapPrinter.printMindmap(mindmap)
MindmapPrinter.printNodes(mindmap)

print('\n')
#here, the c.setMarker(x) effect should be gone too, due to the contained removal.
#This should be handled on the model/node level
mindmap.removeMarker(x)
MindmapPrinter.printMindmap(mindmap)
MindmapPrinter.printNodes(mindmap)