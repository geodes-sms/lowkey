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

#Create a Marker
x = Marker('x')
mindmap.addMarker(x)
c.setMarker(x)

#Print the MindMap
MindmapPrinter.printMindmap(mindmap)
MindmapPrinter.printNodes(mindmap)

print('\n')
mindmap.removeMarker(x)  #here, the c.setMarker(x) effect should be gone too, due to the contained removal. This should be handled on the model/node level
MindmapPrinter.printMindmap(mindmap)
MindmapPrinter.printNodes(mindmap)