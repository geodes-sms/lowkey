#!/usr/bin/env python
import time

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Time utility.
"""

def current() -> int:
    return round(time.time() * 1000)