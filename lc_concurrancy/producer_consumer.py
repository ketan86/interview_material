import queue
import threading

EXIT = False
class ProducerThread(threading.Thread):
    
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue


    def run(self):
        global EXIT
        for item in range(10):
            print(f'Producing {item=}: Thread: {self.name}')
            self.queue.put(item, block=True)

        EXIT = True

class ConsumerThread(threading.Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue

    def run(self):
        global EXIT
        while True:
            if EXIT and self.queue.empty():
                break
            item = self.queue.get(block=True)
            print(f'Consuming {item=}: Thread: {self.name}')

q = queue.Queue(10)
p = ProducerThread('producer', q)
c = ConsumerThread('consumer', q)
p.start()
c.start()
p.join()
c.join()


class ProducerThread(threading.Thread):
    
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue


    def run(self):
        for item in range(10):
            print(f'Producing {item=}: Thread: {self.name}')
            self.queue.put(item, block=True)

        print('Done producing items')

class ConsumerThread(threading.Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get(block=True)
            print(f'Consuming {item=}: Thread: {self.name}')

        print('Done consuming item')

q = queue.Queue(10)
p = ProducerThread('producer', q)
c = ConsumerThread('consumer', q)
c.setDaemon(True)
p.start()
c.start()
p.join()