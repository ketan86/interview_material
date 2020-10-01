import socket
from threading import Thread, Lock
import time 
import random
import sys 

class ChatClient:
    def __init__(self, name, server_host, server_port):
        self.name = name
        self.server_port = server_port
        self.server_host = server_host
    
    def run_client(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((self.server_host, self.server_port))

        # register and receive ack
        server.send("register,{0}".format(self.name).encode())
        
        # wait for friends to join
        time.sleep(10)

        # get list of friends
        server.send("list,friends".encode())
        friends = server.recv(1024).decode().split(',')

        while True:
            # randomly select friend and send a message
            friend = friends[random.randint(0, len(friends) - 1 )]
            server.send("chat,{0}".format(friend).encode())
            msg = server.recv(1024)
            print('friend {0} said: {1}'.format(self.name, msg.decode()))
            # time.sleep(random.randint(2,6))


if __name__ == '__main__':
    server = ChatClient(sys.argv[1], '127.0.0.1', 8080)
    server.run_client()
