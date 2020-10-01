"""
Asyncio already provides us with an API to sleep asynchronously
asyncio.sleep(). In fact, this is one of the most commonly used asyn APIs in
introductory examples explaining async.io. The problem at hand is to implement
our own coroutine that sleeps asynchronously. The signature of the coroutine is
as follows.

    # Implement the following coroutine where
    # sleep_for is defined in seconds
    async def asleep(sleep_for):
        pass

This makes for an excellent interview problem as it is small enough to be
completed in an hour and tricky enough to test a candidate's thought-process.


Solution The first thought to cross your mind will be to use time.sleep() API
to wait out the requested sleeping time. However, the API is a blocking one and
will block the thread that executes it. Obviously, this rules out invoking the
API using the main thread. But it doesn't preclude us from executing this API
on a different thread.

This insight leads us to a possible solution. We can create a Future object and
await it in the asleep() coroutine. The only requirement is now to have another
thread resolve the future after sleep_for seconds have elapsed. The partial
solution looks as follows:
"""
from threading import Thread, current_thread
from asyncio import Future
import asyncio
import time 

async def asleep(t):
    f = Future()
    Thread(target=sync_sleep, args=(t, f)).start()
    await f

def sync_sleep(t, f):
    # sleep syncronously 
    time.sleep(t)

    # resolve future
    f.set_result(None)

    print("Sleeping completed in {0}".format(current_thread().getName()), flush=True)
    
if __name__ == '__main__':
    # start = time.time()
    # asyncio.run(asleep(5))
    # print("main program exiting after running for {0}".format(time.time() - start))
    pass

"""
Surprisingly, the above program hangs and doesn't complete even though the
message from the method sync_sleep() is printed. Somehow the coroutine asleep()
is never resumed after the future it is awaiting has been resolved. The reason
is that Future isn't thread-safe. Fortunately, asyncio provides a method to
execute a coroutine on a given loop in a thread-safe manner. The API is
run_coroutine_threadsafe().

So we have a way to resolve the future in a thread-safe manner however, we need
to do that in yet another coroutine since the API run_coroutine_threadsafe()
takes in only coroutines. This requires us to slightly modify our sync_sleep()
method as follows:
"""
async def asleep(t):
    f = Future()
    loop = asyncio.get_event_loop()
    Thread(target=sync_sleep, args=(loop, t, f)).start()
    print('awaiting for future to resolve')
    await f

def sync_sleep(loop, t, f):
    # sleep syncronously 
    time.sleep(t)

    async def sleep_future_resolver(f):
        # resolve future
        f.set_result(None)

    asyncio.run_coroutine_threadsafe(sleep_future_resolver(f), loop)

    print("Sleeping completed in {0}".format(current_thread().getName()), flush=True)
    
if __name__ == '__main__':
    # start = time.time()
    # asyncio.run(asyncio.wait([
    #     asleep(3),
    #     asleep(5),
    #     asleep(6)
    # ]))
    # print("main program exiting after running for {0}".format(time.time() - start))
    pass

"""
using task does not work since task require co-routine
"""

# using thread pool executor
from concurrent.futures import ThreadPoolExecutor

async def asleep(executor, t):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, sync_sleep, t)

def sync_sleep(t):
    time.sleep(t)
    print("Sleeping completed in {0}".format(current_thread().getName()), flush=True)

if __name__ == '__main__':
    # executor = ThreadPoolExecutor(max_workers=3)
    # start = time.time()
    # asyncio.run(asyncio.wait([
    #     asleep(executor, 3),
    #     asleep(executor, 5),
    #     asleep(executor, 6)
    # ]))
    # print("main program exiting after running for {0}".format(time.time() - start))
    pass 

# using process pool executor
# takes slightly longer than the threadpool executor due to overhead of 
# creating processes
from concurrent.futures import ProcessPoolExecutor

async def asleep(executor, t):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, sync_sleep, t)

def sync_sleep(t):
    time.sleep(t)
    print("Sleeping completed in {0}".format(current_thread().getName()), flush=True)

if __name__ == '__main__':
    # executor = ProcessPoolExecutor(max_workers=3)
    # start = time.time()
    # asyncio.run(asyncio.wait([
    #     asleep(executor, 3),
    #     asleep(executor, 5),
    #     asleep(executor, 6)
    # ]))
    # print("main program exiting after running for {0}".format(time.time() - start))
    pass

"""
Reducing the max_worker to 1 in both versions, make the program works
synchronously.
"""
from concurrent.futures import ProcessPoolExecutor

async def asleep(executor, t):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, sync_sleep, t)

def sync_sleep(t):
    time.sleep(t)
    print("Sleeping completed in {0}".format(current_thread().getName()), flush=True)

if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=1)
    start = time.time()
    asyncio.run(asyncio.wait([
        asleep(executor, 3),
        asleep(executor, 5),
        asleep(executor, 6)
    ]))
    print("main program exiting after running for {0}".format(time.time() - start))


"""
The output shows that sleeping takes place in the threads we spawn and not the
main thread. Furthermore, even though we submit the asleep() coroutine five
times to sleep for five seconds each but the total runtime of the program is
roughly five seconds as it should be if we implemented the solution correctly.

As an exercise consider what would happen if we created five threads and had
each thread invoke time.sleep(), will the program in that case take five or
twenty five seconds to complete? Run the code widget below and observe the time
taken by thee program to complete.
"""
from threading import Thread
from threading import current_thread
import time


def sync_sleep(sleep_for):
    time.sleep(sleep_for)
    print("Sleeping completed in {0}".format(current_thread().getName()))


if __name__ == "__main__":
    # start = time.time()

    # threads = list()

    # for _ in range(0, 5):
    #     threads.append(Thread(target=sync_sleep, args=(5,)))

    # for thread in threads:
    #     thread.start()

    # for thread in threads:
    #     thread.join()
    pass

"""
The synchronous sleep test still takes five seconds to complete! You may wonder
what is the difference between our asynchronous sleep versus synchronous sleep
programs? The answer is the asynchronous sleep call is non-blocking whereas the
synchronous sleep call is blocking. Internally though, the scheduler on seeing
a thread is about to block on a sleep call for five seconds, switches it out
for another thread and only resumes executing it after at least five seconds
have elapsed.
"""