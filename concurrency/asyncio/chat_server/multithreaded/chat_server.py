"""
Problem: 

Let's embark on a more realist albeit toy-example of creating a server
that enables instant messaging or chatting among various participants. You may
consider this problem a dumbed-down version of full-blown real life chat room
servers.

Solution: 

We can implement our chat server using either a multithreaded approach
or a single-threaded asyncio-based approach. We'll explore and implement both
the approaches and contrast them at the end.

Our chat server only allows three operations and receives them as commands.

register: A client can register with the server by sending a comma separated
command string "register,<username>", where username is the name of the client
intending to register.

list: A client can retrieve the list of other clients already registered on the
server by sending the command string "list,friends". The client receives a
comma-separated string of usernames including its own.

chat: A client can request a chat message be sent to a friend using the command
string "chat,<username>", where username is an existing registered client on
the server.

Important Note The reader might find us making assumptions and taking shortcuts
in the implementations we present. The reason is that our emphasis isn't on the
networking aspects of the problem or its stability. Rather, the focus is on
illuminating the differences between the two concurrency paradigms. We'll call
out the simplifications and assumptions we make as we go along.

More generally, the implementations we present work for the happy paths we
discuss. For example, we don't test for a client trying to erroneous input or
attempting multiple register requests, etc. Also, the implementations run a
simulation where the connected clients randomly chat with each other and we
don't implement a graceful shutdown. We want the reader to be focused on the
meat of the lesson here rather than be distracted by the niceties of a fully
working solution.
"""


"""
Multithreaded Approach:

In the multithreaded approach, we'll have a main thread
that listens for incoming connections. Once a client connects, the main thread
spawns a worker thread that maintains a persistent connection with the client
and handles all future requests from the same client. This is in line with how
web-servers generally handle incoming requests. The choices include forking the
current process to deal with a new request or handing-off the client request to
a pool of worker threads. It should be obvious to the reader that the main
thread can't risk handling a client request as it can drop new incoming
connections during the time it spends processing the current client's request.
The main thread's logic appears below:
"""
import socket
from threading import Thread, Lock
import time 
import random

class ChatServer:

    def __init__(self, port):
        self.port = port
        self.lock = Lock()
        self.clients = {}

    def handle_client(self, client):
        user = 'unknown'
        while True:
            data = client.recv(1024).decode()
            command, param = data.split(",")

            if command == 'register':
                print("\n{0} registered\n".format(param))
                with self.lock:
                    self.clients[param] = client
            
            if command == 'list':
                with self.lock:
                    names = self.clients.keys()
                    client.send(','.join(names).encode())
            
            if command == 'chat':
                to_socket = None
                with self.lock:
                    if param in self.clients:
                        to_socket = self.clients[param]
                if to_socket:
                    to_socket.send(("{0} says hi".format(param)).encode())
                else:
                    print("\nNo user by the name <{0}>\n".format(param))

    def run_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', self.port))
        server.listen()
        while True:
            client, address = server.accept()
            ct = Thread(target=self.handle_client, args=(client,), daemon=True)
            ct.start()



if __name__ == '__main__':
    server = ChatServer(8080)
    server.run_server()
