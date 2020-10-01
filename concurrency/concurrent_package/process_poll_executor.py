"""
ProcessPoolExecutor:

The process pool is very similar to a thread pool except
that it is pool of processes that execute the task rather than threads. Let's
rewrite one of the previous examples using a process pool instead of a thread
pool.
"""

from concurrent.futures import ProcessPoolExecutor
import multiprocessing
from multiprocessing import current_process
from threading import current_thread
 
import os
 
 
def say_hi(item):
    print(
        "\nhi " + str(item) + " executed in thread id " + current_thread().name + " in process id " + str(
            os.getpid()) + " with name " + current_process().name,
        flush=True)
 
 
if __name__ == '__main__':
    # print("Main process id " + str(os.getpid()))
    # multiprocessing.set_start_method('spawn')
    # executor = ProcessPoolExecutor(max_workers=10)
    # lst = list()
    # for i in range(1, 10):
    #     lst.append(executor.submit(say_hi, "guest" + str(i)))
 
    # for future in lst:
    #     future.result()
 
    # executor.shutdown()
    pass

"""
Note that we can either have the processes spawned or forked by the process
pool by setting the start method appropriately. If you change the start method
to fork on line#18 in the above example, the output would show that the
processes were forked.

We can also use the map() API with the process pool. We redo the threadpool
example using a processpool below.
"""

from concurrent.futures import ProcessPoolExecutor
import os
import time


def square(item):
    print("Executed in process with id " + str(os.getpid()), flush=True)
    return item * item


if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=10)

    it = executor.map(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), chunksize=1)

    for sq in it:
        print(sq)

    executor.shutdown()


"""
The only major difference when using map() with threads vs processes is the
effect of the chunksize argument. In the above example, we have set the
chunksize to one which implies each square will be calculated by a different
process. If we change the chunksize to five then we only require two processes
to square the ten input values. Depending on the usecase it may happen that a
chunksize set to a higher value results in faster execution as time is saved in
creating and then tearing down more number of processes.
"""