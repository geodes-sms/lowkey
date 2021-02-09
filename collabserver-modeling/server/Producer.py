#!/usr/bin/env python
import asyncio
import json

import websockets

from server import Commands

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Message producer component for CollabClients.
"""


class Procuder():
    
    async def produce(self, message:str):
        async with websockets.connect("ws://localhost:8765") as ws:
            await ws.send(message)
            await ws.recv()
    
    def readUserInput(self):
        while True:
            userInput = str(input(">"))
            if not userInput:
                continue
            
            arguments = userInput.split()
            command = arguments[0]
                        
            if not Commands.valid(command):
                print("Invalid command")
            else:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(producer.produce(message=userInput))
                
    def jsonify(self, userInput):
        params = {}
        params['command'] = userInput
        return json.dumps(params)

    
if __name__ == "__main__":
    producer = Procuder()
    producer.readUserInput()
