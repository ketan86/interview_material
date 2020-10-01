"""
Asynchronous Implementation:

The asynchronous paradigm to implement a chat
server involves using a single thread, usually called the event loop. In the
case of Python, we'll not implement an event loop from scratch rather leverage
asyncio module for the job.

Similar to the multithreaded approach, we need an entity to continuously listen
for new incoming connections. We'll use the asyncio's start_server() coroutine.
The coroutine takes in the server's hostname and a port to listen for incoming
connections on. Once a client connects with the server, the coroutine invokes a
user-specified callback to invoke. The callback includes the details to read
and write from the connected client. The code snippet to start the server would
look like as follows:
"""
from threading import current_thread
import asyncio


class ChatServer:

    def __init__(self, port):
        self.port = port
        self.clients = {}
        self.writers = {}
    

    async def handle_client(self, msg, writer):
        command, param = msg.split(',')
        if command == 'register':
            print("\n{0} registered -- {1}\n".format(param, current_thread().getName()))
            self.clients[param] = writer
            self.writers[writer] = param

            # send ack
            import pdb;pdb.set_trace()
            writer.write('ack'.encode())
            await writer.drain()

        if command == 'chat':
            to_writer = None
            if param in self.clients:
                to_writer = self.clients[param]
            
            if to_writer:
                to_writer.write(
                    ("{0} says hi".format(self.writers[writer])).encode())
            else:
                print("\nNo user by the name |{0}|\n".format(param))

        if command == 'list':
            names = self.clients.keys()
            writer.write(','.join(names).encode())
            await writer.drain()

    async def new_connection(self, reader, writer):
        while True:
            data = await reader.read(1024)
            msg = data.decode()
            print("\nserver received: {0} -- {1}\n".format(
                    msg, current_thread().getName()))
            await self.handle_client(msg, writer)

async def main():
    host, port = '127.0.0.1', '8080'
    server = ChatServer(8080)
    server = await asyncio.start_server(server.new_connection, host, port)
    await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())