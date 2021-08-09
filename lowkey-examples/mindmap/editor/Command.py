#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""TODO: Description goes here.
"""

import logging


class Command():
    
    def execute(self):
        logging.debug("Executing abstract command")
