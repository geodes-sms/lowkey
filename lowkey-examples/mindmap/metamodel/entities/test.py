#!/usr/bin/env python

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

import MindMapFactory

t = MindMapFactory.factory('topic')
print(t)