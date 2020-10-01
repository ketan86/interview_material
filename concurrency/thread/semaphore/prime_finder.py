from threading import Thread, current_thread, Semaphore
import time

exit_flag = False
prime_holder = None
print_sema = Semaphore(0)
find_sema = Semaphore(0)

def is_prime(num):
    if num == 2 or num == 3:
        return True
 
    div = 2
 
    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1
    return True

def printer_thread():
    global prime_holder

    while not exit_flag:
        # wait for print semaphore to release by finder thread
        print('waiting for prime number to be found')
        print_sema.acquire()
        print('{} is a prime number'.format(prime_holder))
        # release find semaphore so finder thread can continue
        print('notifying the finder thread for next prime number')
        find_sema.release()

def finder_thread():
    global prime_holder

    i = 0
    while not exit_flag:
        while not is_prime(i):
            i += 1
            time.sleep(5)

        prime_holder = i
        print('nofiying printer thread')
        # prime is found, signal the printer thread by releasing semaphore
        print_sema.release()

        print('wait for printer thread to print and notify')
        # block finder thread
        find_sema.acquire()
            
        i += 1
    
printer_thread = Thread(target=printer_thread)
printer_thread.start()

finder_thread = Thread(target=finder_thread)
finder_thread.start()

# let the thread run for 3 seconds
time.sleep(3)

exit_flag = True

printer_thread.join()
finder_thread.join()