"""
In the previous sections, we studied how to create and manage threads and
processes. However, managing these entities can be taxing on the developer so
Python alleviates this burden by providing an interface which abstracts away
the subtleties of starting and tearing down threads or processes. The
concurrent.futures package provides the Executor interface which can be used to
submit tasks to either threads or processes. The two subclasses are:

ThreadPoolExecutor

ProcessPoolExecutor

Tasks can be submitted synchronously or asynchronously to the pools for
execution.
"""

"""
ThreadPoolExecutor:

The ThreadPoolExecutor uses threads for executing submitted
tasks. Let's look at a very simple example.
"""
from concurrent.futures import  ThreadPoolExecutor
from threading import current_thread

def say_hi(item):
    print("\nhi " + str(item) + " executed in thread id " + current_thread().name, flush=True)

if __name__ == '__main__':
    # executor = ThreadPoolExecutor(max_workers=10)
    # futures = []
    # for i in range(1, 10):
    #     futures.append(executor.submit(say_hi, 'guest {}'.format(str(i))))

    # for f in futures:
    #     f.result()

    # executor.shutdown()
    pass

"""
We create a thread pool with a maximum of ten threads. Next, we run in a loop
and submit tasks to be executed. The first argument to the submit() is a
callable which gets invoked with the arguments that follow. If you examine the
output you'll see that tasks are executed by threads with different names. The
submit calls return what we call a future. The Future class represents the
execution of the callable. Note that the invocation future.result() is
blocking. Interestingly, if we change the code within the first for loop as
follows, the execution becomes serial.

   for i in range(1, 10):
        future = executor.submit(say_hi, "guest" + str(i))
        future.result()

"""


"""
map:

The map() returns an iterator over the results of applying a function to a list
of values. Both the function and the values are passed-in as parameters to the
map() call. The results are returned in-order of the input values. Consider the
following snippet:

    executor = ThreadPoolExecutor(max_workers=10)
    it = executor.map(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                     chunksize=1, timeout=2)



In our example square() is the callable. Internally, the iterator's __next()__
calls the result() method of the future, which is a blocking call. If the
result isn't ready for one of the futures, the iteration will block. To
mitigate this situation, we can specify a timeout value in the map call and if
the result isn't ready after timeout number of seconds have elapsed, a Timeout
exception is raised. We are able to iterate over the futures which have
completed but the first future encountered whose computation hasn't completed
will result in blocking the iteration.

In the example below, we simulate a timeout exception by sleeping for ten
seconds for the fifth computation in the callable whilst the timeout is set to
two seconds in the map() call. If you run the example you'll see the results of
the first four futures printed before a timeout exception is raised.

Also note that if you don't specify the timeout argument in the map call, the
iteration would simply block the fifth time until the fifth future completes.
"""
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time


def square(item):
    print('processing item {} in {}'.format(item, current_thread().name))
    if item == 5:
        time.sleep(10)
    return item * item


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=10)

    it = executor.map(square, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                     chunksize=1, timeout=2)

    for sq in it:
        print(sq)

    executor.shutdown()

"""
In the above two examples, even though the main thread exits when it receives
the timeout exception, however, the python program doesn't exit until the
thread executing the fifth computation also exists. If the thread were a daemon
thread then the program could exit without waiting for the thread to complete.
Lastly, note that the argument chunksize will have no effect when used with a
thread pool.
"""