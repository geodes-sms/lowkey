#!/usr/bin/env python
import logging
import time

from network.Session import Session

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

logging.basicConfig(level=logging.INFO)
session = Session()
        
"""
Give time to the ZMQ elements being set up. Might require higher values in real distributed
settings. A synchronous setup workflow might be more appropriate here. 
"""
time.sleep(.2)

session.createEntity("entity1")
