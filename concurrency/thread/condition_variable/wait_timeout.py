from threading import Condition
from threading import Thread
import time

flag = False

cond_var = Condition()


def child_task():
    cond_var.acquire()

    if (flag == False):
        cond_var.wait(1)

    if (flag == False):
        print("child thread times out waiting for a notification")

    # don't forget to release the lock
    cond_var.release()


thread = Thread(target=child_task)
thread.start()

time.sleep(3)
thread.join()
