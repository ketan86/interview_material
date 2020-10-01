"""
An event object is one of the simplest primitives available for
synchronization. Internally, it has a boolean flag that can be set or unset
using the methods set() and clear(). Additionally, a thread can check if the
flag is set to true by invoking the is_set() method.

The event object exposes a wait() method that threads can invoke to wait for
the internal boolean flag to become true. If the flag is already true, the
thread returns immediately. If there are multiple threads waiting on the event
object and an active thread sets the flag then all the waiting threads are
unblocked.

Event is a convenience class and a wrapper over a condition variable with a
boolean predicate. This is the most common setup for many cooperating threads
where two or more threads coordinate among themselves on a boolean predicate.

Differences with Semaphores Event objects may seem similar to semaphore or a
bounded semaphore but there are slight differences:

An unbounded semaphore can have its internal counter incremented as many times
as acquire() is invoked on it, whereas an event object maintains an internal
boolean flag that can only flip between two state: set or unset.

Can a bounded semaphore intialized to 1 be equivalent to an event object? The
answer is no because the bounded semaphore will raise a ValueError if the
bounded semaphore is acquired more number of times than the initial passed in
capacity. Also acquiring a semaphore decrements the internal counter of the
semaphore whereas waiting on an event object doesn't change the state of the
internal boolean flag.

A thread never gets blocked on wait() of an event object if the internal flag
is set to true no matter how many times the thread invokes the wait() method.>s
"""
from threading import Thread
from threading import Event
import time


def task1():
    # all waiting threads unblock when event is set
    print('waiting for the event to set')
    event.wait()
    print('event set one time')
    print('waiting for the event to set')
    event.wait()
    print('event set second time')
    print('waiting for the event to set')
    event.wait()
    print('event set third time')
    print("thread invoked wait() thrice")
    event.set()

def task2():
    time.sleep(1)
    print('setting the event')
    event.set()
    print('event is set')
    event.wait()
    print('unblocked by task1')


event = Event()

thread1 = Thread(target=task1)
thread1.start()

thread2 = Thread(target=task2)
thread2.start()

thread1.join()
thread2.join()
