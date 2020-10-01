"""
Notice we aren't using any synchronization primitives in the program above. Not
even locks to guard writes to shared variables. The program goes through two
states, finding primes and then printing them, and repeats the sequence. The
above program would work because there are only two threads involved but would
fail with greater than two threads. Folks with Java background would realize
that a similar program in Java wouldn't work given the memory model of Java,
and would likely require the shared variables to be marked volatile.

The above program is essentially a producer-consumer problem. The printer
thread is a consumer and the finder thread is a producer. The printer thread
needs to be signaled somehow that a prime number has been discovered for it to
print. Do you see a condition here? The condition in our program is the
discovery of the prime number represented by the boolean variable found_prime.
Realize that locks don't help us signal other threads when a condition becomes
true.

One shortcoming of the above code is we have the printer thread constantly
polling in a while loop for the found_prime variable to become true. This is
called busy waiting and is highly discouraged as it unnecessarily wastes CPU
cycles. Ideally, the printer thread should go to sleep so that it doesn't
consume any system resources and be woken up when the condition it needs to act
upon becomes true. This can be achieved through condition variables.

In the next section, we'll see how to use condition variables.
"""


"""
We create a condition variable as follows:

Creating a condition variable cond_var = Condition() The two important
methods of a condition variable are:

wait() - invoked to make a thread sleep and give up resources

notify() - invoked by a thread when a condition becomes true and the
invoking threads want to inform the waiting thread or threads to proceed

A condition variable is always associated with a lock. The lock can be
either reentrant or a plain vanilla lock. The associated lock must be
acquired before a thread can invoke wait()or notify() on the condition
variable.

Incorrect way of using condition variables cond_var = Condition()
cond_var.wait()  # throws an error
"""
from threading import Thread, Condition, current_thread

cond_var = Condition()


import time

found_prime = False
prime_holder = None
exit_flag = False


def printer_thread_func():
    global prime_holder
    global found_prime

    while not exit_flag:
        
        # wait for the prime number to be found and if wake up and 
        # print the prime number.
        with cond_var:
            while not found_prime:
                # lock is given up until thread is awake and reacquires the lock.
                cond_var.wait()
        
        print('{} is a prime number.'.format(prime_holder))

        # set found prime to False and notify the finder thread about
        # the next prime number.
        with cond_var:
            found_prime = False
            cond_var.notify()

def finder_thread_func():
    global prime_holder
    global found_prime
 
    i = 1

    while not exit_flag:

        while not is_prime(i):
            i += 1
            time.sleep(.01)


        prime_holder = i
        # if prime is found, notify the printer thread
        # we take the lock so if found prime flag is set,
        # we also notify the printe thread. if printer
        # thread is not waiting, notify does not do anything.
        with cond_var:
            found_prime = True
            cond_var.notify()
            # we could notify and set found_prime to True and that will
            # work since we hold the lock.

        # wait until printer thread prints the prime number and
        # notify the thread to continue.
        with cond_var:
            # while loop prevents the thread from being woken up even when
            # condition is not true.
            while found_prime and not exit_flag:
                cond_var.wait()
    
        i += 1

    print("finder exiting")

def is_prime(n):
    
    if n == 2 or n == 3:
        return True
    div = 2
 
    while div <= n / 2:
        if n % div == 0:
            return False
        div += 1
 
    return True

# single printer thread
# printer_thread = Thread(target=printer_thread_func)
# printer_thread.start()

# finder_thread = Thread(target=finder_thread_func)
# finder_thread.start()

# # Let the threads run for 5 seconds
# time.sleep(3)
 
# # Let the threads exit
# exit_flag = True
 
# printer_thread.join()
# finder_thread.join()



def two_printer_thread_func():
    global prime_holder
    global found_prime

    while not exit_flag:
        with cond_var:
            # let the same thread print and update the finder thread
            while not found_prime and not exit_flag:
                cond_var.wait()
            if not exit_flag:
                print('{} is a prime number by thread {}.'.format(prime_holder, current_thread().name))
                found_prime = False
                prime_holder = None
                # notify all to wake up the finder and all other printer threads
                # printer threads will wake up and go back to sleep due to
                # while condition if prime is not found by finder thread yet.
                cond_var.notifyAll()

    print('printer exiting')

def finder_thread_func_notify_all():
    global prime_holder
    global found_prime
 
    i = 1

    while not exit_flag:

        while not is_prime(i):
            i += 1
            time.sleep(.01)


        prime_holder = i
        # if prime is found, notify the printer thread
        # we take the lock so if found prime flag is set,
        # we also notify the printe thread. if printer
        # thread is not waiting, notify does not do anything.
        with cond_var:
            found_prime = True
            # notify only notifies one print thread that is waiting and only
            # one printer thread will print the prime but changing to to
            # notify_all wakes up all printer threads and they all contribute
            # to printing.
            # cond_var.notify()      <--- only wakes up the one printer thread
            cond_var.notify_all()

            # we could notify and set found_prime to True and that will
            # work since we hold the lock.

        # wait until printer thread prints the prime number and
        # notify the thread to continue.
        with cond_var:
            # while loop prevents the thread from being woken up even when
            # condition is not true.
            while found_prime and not exit_flag:
                cond_var.wait()
    
        i += 1

    print("finder exiting")


# two printer threads
printer_thread_1 = Thread(target=two_printer_thread_func)
printer_thread_1.start()

printer_thread_2 = Thread(target=two_printer_thread_func)
printer_thread_2.start()

finder_thread = Thread(target=finder_thread_func_notify_all)
finder_thread.start()

# Let the threads run for 5 seconds
time.sleep(3)
# Let the threads exit
exit_flag = True

# wake all threads from sleeping after setting the exit flag.
with cond_var:
    cond_var.notify_all()

printer_thread_1.join()
printer_thread_2.join()
finder_thread.join()