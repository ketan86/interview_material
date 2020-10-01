
import time, random, asyncio
from threading import current_thread


class User:

    def __init__(self, name, host, port):
        self.name = name
        self.port = port
        self.host = host

    async def receive_messages(self, reader):
        while True:
            message = (await reader.read(4096)).decode()
            print("\n{0} received: {1} -- {2}\n".format(
                self.name, message, current_thread().getName()))

    async def run_client(self):
        

        reader, writer = await asyncio.open_connection(self.host, self.port)

        # register user
        writer.write("register,{0}".format(self.name).encode())
        await writer.drain()

        # read the response
        await reader.read(1024)

        # get list of friends
        writer.write("list,friends".encode())
        await writer.drain()

        # read the response
        friends = (await reader.read(4096)).decode()
        print("Received {0}".format(friends))
 

        # launch coroutine to receive messages
        asyncio.create_task(self.receive_messages(reader))

        friends = friends.split(",")
        num_friends = len(friends)

        while True:
            friend = friends[random.randint(0, num_friends - 1)]
            print("{0} is sending msg to {1} -- {2}".format(
                self.name, friend, current_thread().getName()))
            writer.write("chat,{0}".format(friend).encode())
            await writer.drain()
            await asyncio.sleep(3)


async def main():
    host, port = "127.0.0.1", "8080"
    jane = User("Jane", host, port)
    zak = User("Zak", host, port)
    jane1 = User("Jane1", host, port)
    zak1 = User("Zak1", host, port)
    jane2 = User("Jane2", host, port)
    zak2 = User("Zak2", host, port)
    jane3 = User("Jane3", host, port)
    zak3 = User("Zak3", host, port)
    await asyncio.gather(
        jane.run_client(),zak.run_client(),
        jane1.run_client(),zak1.run_client(),
        jane2.run_client(),zak2.run_client(),
        jane3.run_client(),zak3.run_client())

if __name__ == "__main__":
    # connect client
    asyncio.run(main())