#!/usr/bin/env python

import asyncio

import websockets

from server.Session import Session

__author__ = "Istvan David"
__copyright__ = "Copyright 2021, GEODES"
__credits__ = "Eugene Syriani"
__license__ = "GPL-3.0"

"""
Server component of the CollabServer Python stack.
"""


class Server():
    
    def __init__(self):
        print("Creating server with Model.")
        self.__session = Session()

    async def listen(self, websocket, path):
        request = await websocket.recv()
        print(f"[SERVER] Request received: {request}.")
        
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
        
        response = f"{command.upper()} command executed."

        await websocket.send(response)


        
if __name__ == "__main__":
# import sys;sys.argv = ['', 'Test.testName']
    server = Server()
    start_server = websockets.serve(server.listen, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
