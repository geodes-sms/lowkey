#!/usr/bin/env python

import asyncio
import logging

import websockets
from websockets.server import WebSocketServerProtocol

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Server component of the CollabServer Python stack.
"""


class Server():
    
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    
    def __init__(self):
        print("Creating server.")
        self.__connectedClients = set()
        
    async def register(self, ws:WebSocketServerProtocol) -> None:
        self.__connectedClients.add(ws)
        logging.info(f'{ws.remote_address} connects.')
            
    async def unregister(self, ws:WebSocketServerProtocol) -> None:
        self.__connectedClients.remove(ws)
        logging.info(f'{ws.remote_address} disconnects.')
    
    async def sendToClients(self, message: str) -> None:
        if self.__connectedClients:
            await asyncio.wait([client.send(message) for client in self.__connectedClients])        

    async def wsHandler(self, ws:WebSocketServerProtocol, uri:str) -> None:
        await self.register(ws)
        try:
            await self.distribute(ws)
        finally:
            await self.unregister(ws)
            
    async def distribute(self, ws:WebSocketServerProtocol) -> None:
        async for message in ws:
            await self.sendToClients(message)

        
if __name__ == "__main__":
    server = Server()
    start_server = websockets.serve(server.wsHandler, "localhost", 8765)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)
    loop.run_forever()
