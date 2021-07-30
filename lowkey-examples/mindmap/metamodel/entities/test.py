#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from metamodel import MindMapFactory

t = MindMapFactory.factory('topic')
print(t)
