"""
The third and final option that can be chosen for the start method is the
"forkserver". The official documentation states that with forkserver as the
start method, a brand new single-threaded process, called server is started.
Whenever, a new process needs to be created, the parent process connects to the
server and requests that it forks a new process. Since the server process is
single threaded, it can safely invoke os.fork() to create a new process.

The example below appears from the previous section and now uses the forkserver
as the start method on line 13.
"""

from multiprocessing import Process
import multiprocessing

class Test:
    value = 777


def process_task():
    print(Test.value)


if __name__ == '__main__':
    # multiprocessing.set_start_method('forkserver')

    # # change the value of Test.value before creating
    # # a new process
    # Test.value = 999
    # process = Process(target=process_task, name="process-1")
    # process.start()
    # process.join()
    pass

"""
You can verify on your system that a new server process gets created, when we
select the start method as forkserver. Note forkserver doesn't work on a
Windows system but for others, you may want to save the following script in a
file and run it. Make sure your version of python is atleast 3.6+
"""

from multiprocessing import Process
import multiprocessing
import time
 
 
def process_task():
    # block the new process
    time.sleep(1000 * 1000)
 
 
if __name__ == '__main__':
    multiprocessing.set_start_method('forkserver')
 
    process = Process(target=process_task)
    process.start()
    print("New process created")
    # block the main process too
    process.join()

"""
Run the above script in your terminal and the program would hang. Next execute
"ps -aef | grep python" in a new terminal window. The output should list the
python processes. Below, I share the screen-shot on my machine with python
processes highlighted.

If you run the suggested command, you should see four python processes (not
counting the grep). One is the parent process, second the child process, third
the forkserver process and fourth a semaphore tracker process.

Semaphore Tracker The semaphore tracker process gets created with both spawn
and forkserver as start methods. There is a limit on the number of semaphores
that can exist on a Unix based system. Semaphores when created by a process are
linked to that process and may remain linked even if the process exits in an
abnormal way e.g. it is killed. The semaphore tracker process is tasked with
making sure there are no leaking semaphores i.e. it unlinks semaphores which
were linked to processes that have already exited.
"""