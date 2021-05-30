"""
Print series 010203040506. Using multi-threading
    1st thread will print only 0
    2nd thread will print only even numbers and
    3rd thread print only odd numbers.
"""

import threading

class PrintSeries:

    def __init__(self, n):
        self.zero_semaphore = threading.Semaphore(1)
        self.even_semaphore = threading.Semaphore(0)
        self.odd_semaphore = threading.Semaphore(0)
        self.n = n

    def print_zero(self):
        for i in range(self.n):
            self.zero_semaphore.acquire()
            if i == 0:
                print(i)
                self.zero_semaphore.release()
            elif i % 2 == 0:
                self.even_semaphore.release()
            elif i % 2 != 0:
                self.odd_semaphore.release()

    def print_even(self):
        for i in range(2, self.n, 2):
            self.even_semaphore.acquire()
            print(i)
            self.zero_semaphore.release()

    def print_odd(self):
        for i in range(1, self.n, 2):
            self.odd_semaphore.acquire()
            print(i)
            self.zero_semaphore.release()

threads = []

p = PrintSeries(10)
t = threading.Thread(target=p.print_zero)
t2 = threading.Thread(target=p.print_even)
t3 = threading.Thread(target=p.print_odd)
threads.append(t)
threads.append(t2)
threads.append(t3)
t.start()
t2.start()
t3.start()
for t in threads:
    t.join()
