"""
Python offers the ability to execute tasks as processes using the
multiprocessing module. Most of the APIs in the module mirror the APIs found in
the threading module. In fact if you have a program written using the threading
module APIs, it is trivial to change the program to work with the
multiprocessing module.

The limitations of the global interpreter lock are to an extent addressed by
the multiprocessing module. One of the most common critiques of Python has been
its inability to schedule threads on multiple processors in a multicore system.
So much so, that alternative implementations such as Jython, IronPython, etc
have cropped up to address this shortcoming of the standard Python
implementation. The multiprocessing module offers hope by allowing a program to
spin-off tasks as separate processes that can then run on individual
processors. This allows Python to be both concurrent and parallel, whereas with
the threading module, Python is only concurrent and not parallel. Languages
without a GIL in their design, such as Java, can exhibit both concurrency and
parallelism using only threads on a multicore system.

Creating, managing and tearing down processes is more expensive than doing the
same for threads. Furthermore, inter-process communication is relatively slower
than inter-thread communication. Both these drawbacks may not make Python a
practical technology choice for super-critical or time-sensitive use-cases.

Given the above context, let's explore the multiprocessing module and the APIs
it offers.


A process is a program in execution and operating systems provide different
ways of creating new processes. Furthermore, each operating system has its own
nuances when spawning new processes, which gets reflected in Python's APIs. The
multiprocessing module offers the method set_start_method() to let the
developer choose the way new processes are created. There are three of them:

fork

spawn

fork-server

Example The multiprocessing module exposes APIs very similarly to the threading
module to create processes. The constructor of the Process class accepts a
callable object that the spawned process then executes. Below is an example of
creating three different processes:
"""

from multiprocessing import Process
from multiprocessing import current_process
import os
 
 
def process_task():
    print("{0} has pid: {1} with parent pid: {2}".format(current_process().name, os.getpid(), os.getppid()))
 
 
process = [0] * 3
 
for i in range(0, 3):
    process[i] = Process(target=process_task, name="process-{0}".format(i))
    process[i].start()
 
for i in range(0, 3):
    process[i].join()
 
print("{0} has pid: {1} ".format(current_process().name, os.getpid()))


"""
Note that in the above output, each process prints the pid (process id) that is
assigned to it by the underlying operating system. The main process also prints
its pid which is also the parent id of the spawned processes.

Passing arguments to processes Similar to the threading module, we can pass
arguments to a spawned process as a list of arguments or/and keyword
dictionary. An example is given below:

Passing arguments to processes
"""

from multiprocessing import Process
from multiprocessing import current_process
import os
 
 
def process_task(x, y, z, key1, key2):
    print("\n{0} has pid: {1} with parent pid: {2}".format(current_process().name, os.getpid(), os.getppid()))
    print("Received arguemnts {0} {1} {2} {3} {4}\n".format(x, y, z, key1, key2))
 
 
process = Process(target=process_task,
                  name="process-1",
                  args=(1, 2, 3),
                  kwargs={
                      'key1': 'arg1',
                      'key2': 'arg2'
                  })
process.start()
 
process.join()
 

"""
In the above examples, we don't specify set_start_method() and let Python
choose the default.
"""