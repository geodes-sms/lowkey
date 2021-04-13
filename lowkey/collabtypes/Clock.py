#!/usr/bin/env python
import enum
import time

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Clock facility supporting DEBUG mode without boilerplate.
"""


class ClockMode(enum.Enum):
    REAL = 0
    DEBUG = 1


class Clock:
    
    __step = 1000000000 
    __instance = None
    __mode = ClockMode.REAL
    __debugTime = 0
    
    @staticmethod
    def setUp(mode=ClockMode.REAL):
        if Clock.__instance == None:
            Clock(mode)
        return Clock.__instance
    
    def __init__(self, mode):
        if Clock.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Clock.__instance = self
            Clock.__mode = mode
            if mode == ClockMode.DEBUG:
                self.__debugTime = self.__currentRealTime()
                print("Clock in DEBUG mode")
    
    def getMode(self):
        return self.__mode
    
    def getStep(self):
        return self.__step
    
    def currentTime(self):
        if self.__mode == ClockMode.REAL:
            return self.__currentRealTime()
        if self.__mode == ClockMode.DEBUG:
            return self.__currentDebugTime()
        
    def __currentRealTime(self):
        return time.time_ns()
    
    def __currentDebugTime(self):
        self.__debugTime += self.__step
        return self.__debugTime
