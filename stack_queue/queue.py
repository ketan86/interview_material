class myQueue:
    def __init__(self):
        self.queueList = []

    def isEmpty(self):
        return self.size() == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.queueList[0]

    def back(self):
        if self.isEmpty():
            return None
        return self.queueList[-1]

    def size(self):
        return len(self.queueList)

    def enqueue(self, value):
        self.queueList.append(value)

    def dequeue(self):
        if self.isEmpty():
            return None
        front = self.front()
        self.queueList.remove(self.front())
        return front
