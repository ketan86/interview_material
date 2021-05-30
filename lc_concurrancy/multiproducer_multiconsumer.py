import time
import threading
import queue
import concurrent.futures as cf


# 10 threads - 10 tasks
def producer(p_queue, c_queue):
    thread_name = threading.current_thread()
    print(f'Running producer thread {thread_name}')
    item = p_queue.get()
    print(f'Produced {item=}: Thread: {thread_name}')
    c_queue.put(item)

def consumer(c_queue):
    thread_name = threading.current_thread()
    print(f'Running consumer thread {thread_name}')
    item = c_queue.get(block=True)
    print(f'Consumed {item=}: Thread: {thread_name}')


# p_queue = queue.Queue(10)
# for item in range(10):
#     p_queue.put(item)

# c_queue = queue.Queue()

# pe = cf.ThreadPoolExecutor(10)
# ce = cf.ThreadPoolExecutor(10)


# ce_futures = []
# for i in range(10):
#     ce_futures.append(ce.submit(consumer, c_queue))

# pe_futures = []
# for i in range(10):
#     pe_futures.append(pe.submit(producer, p_queue, c_queue))


# 5 threads, 10 tasks

EXIT = False
def producer(p_queue, c_queue):
    global EXIT
    thread_name = threading.current_thread()
    print(f'Running producer thread {thread_name}')
    while not p_queue.empty():
        item = p_queue.get()
        print(f'Produced {item=}: Thread: {thread_name}')
        c_queue.put(item)
    EXIT = True
def consumer(p_queue, c_queue):
    global EXIT
    thread_name = threading.current_thread()
    print(f'Running consumer thread {thread_name}')
    while True:
        print(f'Stuck')
        if EXIT and c_queue.empty():
            break
        try:
            item = c_queue.get()
            print(f'Consumed {item=}: Thread: {thread_name}')
        except queue.Empty:
            pass

    # while not p_queue.empty():
    #     try:
    #         item = c_queue.get()
    #         print(f'Consumed {item=}: Thread: {thread_name}')
    #     except queue.Empty:
    #         pass
    
    # while not c_queue.empty():
    #     try:
    #         item = c_queue.get()
    #         print(f'Consumed {item=}: Thread: {thread_name}')
    #     except queue.Empty:
    #         pass

p_queue = queue.Queue(10)
for item in range(10):
    p_queue.put(item)

c_queue = queue.Queue()

pe = cf.ThreadPoolExecutor(5)
ce = cf.ThreadPoolExecutor(5)

ce_futures = []
for i in range(5):
    ce_futures.append(ce.submit(consumer, p_queue, c_queue))

pe_futures = []
for i in range(5):
    pe_futures.append(pe.submit(producer, p_queue, c_queue))

# for pt in pe_futures:
#     pt.result()

# for ct in ce_futures:
#     ct.result()
    