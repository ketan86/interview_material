"""
Lock is the most basic or primitive synchronization construct available in
Python. It offers two methods: acquire() and release(). A Lock object can only
be in two states: locked or unlocked. 

A Lock object is equivalent of a mutex that you read about in operating systems
theory.

Acquire Whenever a Lock object is created it is initialized with the unlocked
state. Any thread can invoke acquire() on the lock object to lock it. Advanced
readers should note that acquire() can only be invoked by a single thread at
any point because the GIL ensures that only one thread is being executed by the
interpreter. This is in contrast to other programming languages with more
robust threading models where multiple threads could be executing on different
cores and theoretically attempt to acquire a lock at exactly the same time.

If a Lock object is already acquired/locked and a thread attempts to acquire()
it, the thread will be blocked till the Lock object is released. If the caller
doesn't want to be blocked indefinitely, a floating point timeout value can be
passed in to the acquire() method. The method returns true if the lock is
successfully acquired and false if not.

Release The release() method will change the state of the Lock object to
unlocked and give a chance to other waiting threads to acquire the lock. If
multiple threads are already blocked on the acquire call then only one
arbitrarily chosen (varies across implementations) thread is allowed to acquire
the Lock object and proceed.

Example An example is presented below where two threads share a list and one of
the threads tries to modify the list while the other attempts to read it. Using
a lock object we make sure that the two threads share the list in a thread-safe
manner.
"""

"""
recursion level ownership A primitive lock (Lock) is a synchronization
primitive that is not owned by a particular thread when locked.

For the repeatable Lock (RLock) In the locked state, some thread owns the lock;
in the unlocked state, no thread owns it. When invoked if this thread already
owns the lock, increment the recursion level by one, and return immediately. if
thread doesn't own the lock It waits until owner release lock. Release a lock,
decrementing the recursion level. If after the decrement it is zero, reset the
lock to unlocked.

Performance I don't think there is some performance difference rather
conceptual one.

Lock can be acquired by any thread and can be released by any thread.
"""

import threading
import time

lock = threading.Lock()


class Worker(threading.Thread):

    def __init__(self, sleep_time):
        super().__init__()
        self.sleep_time = sleep_time

    def run(self):
        print('{} has entered. waiting for lock'.format(
            threading.current_thread().name))
        with lock:
            print('{} has acquired the lock'.format(
                threading.current_thread().name))
            time.sleep(self.sleep_time)


w1 = Worker(4)
w2 = Worker(2)
w1.start()
w2.start()
w1.join()
w2.join()


# DEADLOCK Example
print('==DEADLOCK==')
lock1 = threading.Lock()
lock2 = threading.Lock()


class Worker1(threading.Thread):

    def __init__(self, lock1, lock2):
        super().__init__()
        self.lock1 = lock1
        self.lock2 = lock2

    def run(self):
        with self.lock1:
            print('{} has acquired the lock1'.format(
                threading.current_thread().name))
            print('{} has entered. waiting for lock2'.format(
                threading.current_thread().name))
            time.sleep(2)
            with self.lock2:
                print('{} has acquired the lock2'.format(
                    threading.current_thread().name))
                time.sleep(5)


class Worker2(threading.Thread):

    def __init__(self, lock1, lock2):
        super().__init__()
        self.lock1 = lock1
        self.lock2 = lock2

    def run(self):
        with self.lock2:
            print('{} has acquired the lock2'.format(
                threading.current_thread().name))
            time.sleep(2)

            print('{} has entered. waiting for lock1'.format(
                threading.current_thread().name))
            with self.lock1:
                print('{} has acquired the lock1'.format(
                    threading.current_thread().name))


w1 = Worker1(lock1, lock2)
w2 = Worker2(lock1, lock2)
w1.start()
w2.start()
w1.join()
w2.join()
