#!/usr/bin/env python
import asyncio
import logging

import websockets
from websockets.client import WebSocketClientProtocol

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Message producer component for CollabClients.
"""


class Consumer():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    
    async def consumerHandler(self, websocket: WebSocketClientProtocol) -> None:
        async for message in websocket:
            self.logMessage(message)
    
    async def consume(self):
        async with websockets.connect("ws://localhost:8765") as websocket:
            await self.consumerHandler(websocket)
        
    def logMessage(self, message: str) -> None:
        logging.info(f'Message: {message}.')
        
        """
        arguments = request.split()
        command = arguments[0]
        
        if command.upper() == 'CREATE':
            self.__session.create(arguments[1:])
        elif command.upper() == 'READ':
            self.__session.read(arguments[1:])
        elif command.upper() == 'UPDATE':
            self.__session.update(arguments[1:])
        elif command.upper() == 'DELETE':
            self.__session.delete(arguments[1:])
        else:
            pass
        """


if __name__ == "__main__":
    consumer = Consumer()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consumer.consume())
    loop.run_forever()
