
import time
import random
import threading

class Fork:
    def __init__(self, number):
        self.number = number
        self.condition = threading.Condition(threading.Lock())
        self.taken = False 

    def take(self, user):
        # print(f'{user=} is waiting to lock fork={self.number}')
        with self.condition:
            while self.taken:
                # print(f'{user=} is waiting for fork={self.number}')
                self.condition.wait()
            self.taken = True
            # print(f'fork={self.number} taken by {user=}')

    def drop(self, user):
        # print(f'{user=} is waiting to lock fork={self.number}')
        with self.condition: 
            self.taken = False
            # print(f'fork={self.number} dropped by {user=}')
            self.condition.notify_all()

class Philosopher(threading.Thread):
    """
    In this solution with condition object, we have to make sure the
    access of the fork is not circular for ex,

                    1
                f4       f1
               4          2
                f3      f2
                    3

    1. allowing all users to pick left fork and then right fork

        philosophers = [
        Philosopher(
            i,
            forks[i],
            forks[(i+1) % n]
        ) for i in range(n)]


        user 1 picks f1
        user 2 picks f2
        user 3 picks f3
        user 4 picks f4

        user 1 waiting for f4
        user 2 waiting for f1
        user 3 waiting for f2
        user 4 waiting for f3

        deadlock

    2. allowing all users to pick left fork and then right except
       last user (user4) picks right fork first and then left.

        philosophers = [
            Philosopher(
                i,
                forks[min(i, (i+1) % n)],
                forks[max(i, (i+1) % n)]
            ) for i in range(n)]

        user 1 picks f1
        user 2 picks f2
        user 3 picks f3
        user 4 picks f3 and blocks

        user 1 picks f4
        user 2 waiting for f1
        user 3 waiting for f2
        user 4 waiting for f3

        user 2 and then 3 and then 4 gets chance.

    Using condition variable that allows access to the forks based on
    waiting threads.

    """
    def __init__(self, user, left, right):
        super().__init__()
        self.user = user
        self.left = left
        self.right = right

    def think(self):
        # print(f'user={self.user} thinking...')
        time.sleep(random.randrange(0,2))


    def run(self):
        for i in range(2):
            print(f'user={self.user} is starting to eat..')
            self.left.take(self.user)
            self.think()
            self.right.take(self.user)
            print(f'user={self.user} is eating..')
            self.think()
            self.left.drop(self.user)
            self.think()
            self.right.drop(self.user)
            print(f'user={self.user} is done eating..')

n = 5
forks = [Fork(i) for i in range(n)]

philosophers = [
    Philosopher(
        i,
        # forks[i],
        # forks[(i+1) % n]
        forks[min(i, (i+1) % n)], 
        forks[max(i, (i+1) % n)]
    ) for i in range(n)]

for i in range(n):
    philosophers[i].start()

for i in range(n):
    philosophers[i].join()

