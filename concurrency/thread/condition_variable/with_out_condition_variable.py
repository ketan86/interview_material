"""
Synchronization mechanisms need more than just mutual exclusion; a general need
is to be able to wait for another thread to do something. Condition variables
provide mutual exclusion and the ability for threads to wait for a predicate to
become true.

For Java programmers, the condition variable and its working may seem eerily
familiar and rightly so because the threading module borrows a lot from Java's
concurrency architecture. We'll examine the similarities towards the end of the
lesson. First, let's try to understand why we need condition variables in the
first place.

Why In the previous sections we worked with locks which are used to enforce
serial access to shared state. However, locks aren't enough when threads want
to coordinate among themselves. Imagine a scenario where we have two threads
working together to find prime numbers and print them. Say the first thread
finds the prime number and the second thread is responsible for printing the
found prime. The first thread (finder) sets a boolean flag whenever it
determines an integer is a prime number. The second (printer) thread needs to
know when the finder thread has hit upon a prime number. The naive approach is
to have the printer thread do a busy wait and keep polling for the boolean
value. Let's see what this approach looks like:
"""
from threading import Thread
import time

found_prime = False
prime_holder = None
exit_flag = False


def printer_thread_func():
    global prime_holder
    global found_prime
    while not exit_flag:
        # busy waiting. eating cpu cycles 
        while not found_prime and not exit_flag:
            time.sleep(0.1)
        
        print('{} is a prime number.'.format(prime_holder))

        found_prime = False

def finder_thread_func():
    global prime_holder
    global found_prime
 
    i = 1

    while not exit_flag:

        while not is_prime(i):
            i += 1
        
        prime_holder = i
        found_prime = True

        # busy waiting. eating cpu cycles
        while found_prime and not exit_flag:
            time.sleep(0.1)
        
        i += 1

def is_prime(n):
    if n == 2 or n == 3:
        return True
 
    div = 2
 
    while div <= n / 2:
        if n % div == 0:
            return False
        div += 1
 
    return True


printer_thread = Thread(target=printer_thread_func)
printer_thread.start()
 
finder_thread = Thread(target=finder_thread_func)
finder_thread.start()

# Let the threads run for 5 seconds
time.sleep(3)
 
# Let the threads exit
exit_prog = True
 
printer_thread.join()
finder_thread.join()