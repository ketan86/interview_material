"""
Ownership:

As explained, each reentrant lock is owned by some thread when in
the locked state. Only the owner thread is allowed to exercise a release()
on the lock. If a thread different than the owner invokes release() a
RuntimeError is thrown as shown in the example below:
"""
from threading import RLock
from threading import Thread


def perform_unlock():
    # rlock = RLock()
    rlock.acquire()
    print(rlock)
    print("child task executing")
    rlock.release()


rlock = RLock()

# reentrant lock acquired by main thread
rlock.acquire()
rlock.release()
# let's attempt to unlock using a child thread
thread = Thread(target=perform_unlock)
thread.start()
thread.join()
rlock.acquire()
print(rlock)
