#!/usr/bin/env python
import unittest

import os
import sys
import time

import threading

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from lowkey.collabtypes.Clock import Clock, ClockMode
from metamodel.entities.CentralTopic import CentralTopic
from metamodel.entities.Marker import Marker
from metamodel.entities.MindMap import MindMap
from metamodel.entities.MainTopic import MainTopic
from metamodel.entities.MindMapModel import MindMapModel
from lowkey.network.Server import Server
from editor.Editor import Editor

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"



class CleintServerTests(unittest.TestCase):
    
    def killableRun(self, target):
        target.run()
    
    def setUp(self):
        Clock.setUp(ClockMode.DEBUG)
        
        self._exitEvent = threading.Event()
        
        self._server = Server()
        self._client1 = Editor()
        self._client2 = Editor()
        
        self._threads = []
        
        server_thread = threading.Thread(target=self.killableRun, args=(self._server,))
       # server_thread.daemon = True
        print("Starting server thread")
        server_thread.start()
        self._threads.append(server_thread)
        
        time.sleep(1)
        
        self._client1.join()
        client1_thread = threading.Thread(target=self.killableRun, args=(self._client1,))
       # client1_thread.daemon = True
        print("Starting client1 thread")
        client1_thread.start()
        self._threads.append(client1_thread)
        
        time.sleep(1)
        
        self._client2.join()
        client2_thread = threading.Thread(target=self.killableRun, args=(self._client2,))
       # client2_thread.daemon = True
        print("Starting client2 thread")
        client2_thread.start()
        self._threads.append(client2_thread)
        
        time.sleep(1)
        
    def tearDown(self):
        for t in self._threads:
            del(t)
        del(self._server)
        del(self._client1)
        del(self._client2)
        
    def testCreateModelWithContent(self):
        self._client1.sendUserMessage("create mindmap mm1")
        self._client1.sendUserMessage("read")
        self._client2.sendUserMessage("read")
        
        
if __name__ == "__main__":
    unittest.main()
