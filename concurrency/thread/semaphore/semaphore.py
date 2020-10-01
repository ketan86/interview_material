"""
Semaphore is one of the oldest synchronization primitives, invented by Edsger
Dijkstra. A semaphore is nothing more than an atomic counter that gets
decremented by one whenever acquire() is invoked and incremented by one
whenever release() is called. The semaphore can be initialized with an initial
count value. If none is specified, the semaphore is initialized with a value of
one.

Creating semaphore
# semaphore initialized with a default count of 1
semaphore = Semaphore()

# semaphore initialized with count set to 5
sem_with_count = Semaphore(5)

acquire ( ) If a thread invokes acquire() on a semaphore, the semaphore counter
is decremented by one. If the count is greater than 0, then the thread
immediately returns from the acquire() call. If the semaphore counter is zero
when a thread invokes acquire(), the thread gets blocked till another thread
releases the semaphore.

release ( ) When a thread invokes the release() method, the internal semaphore
counter is incremented by one. If the counter value is zero and another thread
is already blocked on an acquire() then a release would unblock the waiting
thread. If multiple threads are blocked on the semaphore, then one thread is
arbitrarily chosen.

Using Semaphores Semaphores can be used in versatile ways. The primary use of
semaphores is signaling among threads which are working to achieve a common
goal. Consider the below snippet which uses a condition variable between
threads.
"""
# missed signal manifestation

"""
The above program will never exit since the notifying thread notifies before
the first thread has a chance to wait on the condition variable. This is a
manifestation of a missed signal.

You may realize from your reading in the previous sections that the way we are
using the condition variable's wait() method is incorrect. The idiomatic usage
of wait() is in a while loop with an associated boolean condition. For now,
observe the possibility of losing signals between threads.

The faulty program appears in the code widget below:
"""
from threading import Thread, Condition
import time
 
def task1():
    cond_var.acquire()
    cond_var.wait()
    cond_var.release()
 
 
def task2():
    cond_var.acquire()
    cond_var.notify()
    cond_var.release()
 
 
# cond_var = Condition()
 
# # start thread 2 first which invokes notify
# thread2 = Thread(target=task2)
# thread2.start()
 
# # delay starting thread 1 by three seconds
# time.sleep(3)
 
# # start thread 1
# thread1 = Thread(target=task1)
# thread1.start()
 
# thread1.join()
# thread2.join()

# fix above code with semaphore

from threading import Thread, Semaphore
import time

 
# initialize with zero
sem = Semaphore(0)

def task1():
    print('acquiring the lock')
    sem.acquire()
    print('lock acquired')

def task2():
    print('releasing the lock')
    sem.release()
    print('lock released')


# start thread 1
thread1 = Thread(target=task1)
thread1.start()

# start thread 2 first which invokes release()
thread2 = Thread(target=task2)
thread2.start()
 

thread1.join()
thread2.join()