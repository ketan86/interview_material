#
# @lc app=leetcode id=1195 lang=python3
#
# [1195] Fizz Buzz Multithreaded
#

# @lc code=start
from threading import Semaphore


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.fizz_semaphore = Semaphore(0)
        self.buzz_semaphore = Semaphore(0)
        self.fizz_buzz_semaphore = Semaphore(0)
        self.number_semaphore = Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        self.fizz_semaphore.acquire()
        printFizz()
        self.number_semaphore.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        self.buzz_semaphore.acquire()
        printBuzz()
        self.number_semaphore.release()

    # printFizzBuzz() outputs "fizzbuzz"

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        self.fizz_buzz_semaphore.acquire()
        printFizzBuzz()
        self.number_semaphore.release()

    # printNumber(x) outputs "x", where x is an integer.

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.number_semaphore.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.fizz_buzz_semaphore.release()
            elif i % 3 == 0:
                self.fizz_semaphore.release()
            elif i % 5 == 0:
                self.buzz_semaphore.release()
            else:
                printNumber(i)
                self.number_semaphore.release()
# @lc code=end
