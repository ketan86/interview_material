from threading import Thread
from threading import Event
import time
 
 
prime_available = Event()
prime_printed = Event()
prime_holder = None
exit_flag = False

def printer_thread():
    global prime_holder
 
    while not exit_flag:
        # wait for a prime number to become available
        prime_available.wait()
 
        # print the prime number
        print(prime_holder)
        prime_holder = None
 
        # reset the event to false
        prime_available.clear()
 
        # let the finder thread know that printing is done
        prime_printed.set()
 
 
def is_prime(num):
    if num == 2 or num == 3:
        return True
 
    div = 2
 
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True
 
 
def finder_thread():
    global prime_holder
 
    i = 1
 
    while not exit_flag:
 
        while not is_prime(i):
            i += 1
            # Add a timer to slow down the thread
            # so that we can see the output
            time.sleep(.01)
 
        prime_holder = i
 
        # let the printer thread know we have
        # a prime available for printing
        prime_available.set()
 
        # wait for printer thread to print the prime
        prime_printed.wait()
 
        # reset the flag
        prime_printed.clear()
 
        i += 1
 
 
 
 
printerThread = Thread(target=printer_thread)
printerThread.start()
 
finderThread = Thread(target=finder_thread)
finderThread.start()
 
# Let the threads run for 3 seconds
time.sleep(3)
 
exit_flag = True
prime_available.set()
prime_printed.set()
 
printerThread.join()
finderThread.join()