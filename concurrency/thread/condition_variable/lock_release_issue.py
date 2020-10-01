# this program will hung due to first thread who get notified does not 
# release the lock.

from threading import Thread, Condition, current_thread, Lock
import time

flag = False
 
lock = Lock()
cond_var = Condition(lock)


def child_task():
    global flag
    name = current_thread().getName()
 
    cond_var.acquire()
    while not flag:
        cond_var.wait()
        print("\n{0} woken up \n".format(name), flush=True)
 
    print("\n{0} exiting\n".format(name), flush=True)
 
 
if __name__ == "__main__":
    thread1 = Thread(target=child_task, name="thread1")
    thread1.start()
 
    thread2 = Thread(target=child_task, name="thread2")
    thread2.start()
 
    time.sleep(1)
 
    cond_var.acquire()
    flag = True
    cond_var.notify_all()
    cond_var.release()
 
    print("main thread exits", flush=True)
