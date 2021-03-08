#!/usr/bin/env python

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Commands interface.
"""

commands = ['CREATE', 'READ', 'UPDATE', 'DELETE']


def valid(command):
    return command.upper() in commands
