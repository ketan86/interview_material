import threading

"""
# number of alive thread.
active = threading.active_count()

# get current thread ref
current_thread = threading.current_thread()

# get main thread ref
main_thread = threading.main_thread()

# get thread id
id = threading.get_ident()

# get native thread id assigned by kernel
native_id = threading.get_native_id()

# enumerate over all threads
threads = [t for t in threading.enumerate()]

# set trace function. function is passed to sys.settrace() for each thread


def tracer(frame, event, arg):
    # print('tracing...')
    return


threading.settrace(tracer)
thread1 = threading.Thread(target=object)
thread2 = threading.Thread(target=object)
thread1.start()
thread1.join()
thread2.start()
thread2.join()

# stack size used while creating a new thread
stack_size = threading.stack_size()

# max timeout allowed for locking functions
max_timeout = threading.TIMEOUT_MAX

# thread local storage
t_local = threading.local()
if hasattr(t_local, 'x'):
    print('pre: ' + t_local.x)
t_local.x = 'main'
print(threading.current_thread())
print('post: ' + t_local.x)


class Worker(threading.Thread):
    def run(self):
        t2_local = threading.local()
        t2_local.x = 2
        print(threading.current_thread())
        print(threading.current_thread().is_alive())
        if hasattr(t_local, 'x'):
            print('pre: ' + t_local.x)
        t_local.x = self.name
        print('post: ' + t_local.x)


w1, w2 = Worker(), Worker()
w1.start()
w2.start()
# thread would have finished the execution so, is_alive will return False,
# add sleep in thread and this will become True
thread_alive = w1.is_alive()
print(thread_alive)
# any thread can call join on any other thread.
# blocks the caling thread (in this case it's main thread)
w1.join()
w2.join()


# daemon thread. main thread could exit even if daemon thread is alive
class DaemonThread(threading.Thread):

    def run(self):
        import time
        time.sleep(5)
        print('exiting daemon thread now')


dt = DaemonThread(daemon=True)
dt.start()
is_deamon = dt.isDaemon()
# daemon threads are not supposed to ne join. they are left to do some
# processing.
"""

# join with timeout. join can be called multiple times unit
# thread is alive


class TimeoutThread(threading.Thread):

    def run(self):
        import time
        time.sleep(5)
        print('exiting thread now')


tt = TimeoutThread()
tt.start()
tt.join(timeout=1)
while tt.is_alive():
    print('still alive')
    tt.join(timeout=0.5)
print('completed now')


# test without the join
tt = TimeoutThread()
tt.start()
print('doing some other stuff. python process wont exit until threa'
      'finishes execution')
