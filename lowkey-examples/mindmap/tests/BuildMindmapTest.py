#!/usr/bin/env python
import unittest

from collabtypes.Clock import Clock, ClockMode
from mindmap.metamodel.entities.MindMap import MindMap

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"


class BuildMindmapTest(unittest.TestCase):

    def testRenameMindmap(self):
        Clock.setUp(ClockMode.DEBUG)
        
        title1 = 'improveTeachingRecord'
        mindmap = MindMap(title1)
        self.assertEqual(mindmap.getTitle(), title1)
        
        title2 = 'improvePublicationRecord'
        mindmap.setTitle(title2)
        self.assertEqual(mindmap.getTitle(), title2)

        
if __name__ == "__main__":
    unittest.main()
