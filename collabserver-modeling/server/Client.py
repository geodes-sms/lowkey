#!/usr/bin/env python
import asyncio

import websockets
from server import Commands

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Simple command line client facility of the CollabServer Python stack.
"""


class Client():
    
    serverURI = "ws://localhost:8765"

    async def readUserInput(self):
        while True:
            userInput = str(input(">"))
            if not userInput:
                continue
            
            arguments = userInput.split()
            command = arguments[0]
            
            if not Commands.valid(command):
                print("Invalid command")
            else:
                async with websockets.connect(self.serverURI) as websocket:
                    print(f"[CLIENT] Sending request to Server: {userInput}.")
                    await websocket.send(userInput)

                    response = await websocket.recv()
                    print(f"[SERVER] {response}")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    client = Client()
    asyncio.get_event_loop().run_until_complete(client.readUserInput())
