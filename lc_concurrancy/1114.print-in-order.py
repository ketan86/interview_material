#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#

# @lc code=start
from threading import Lock


class Foo:
    def __init__(self):
        """28 ms beats 98.1 % faster"""
        self.first_lock = Lock()
        self.second_lock = Lock()
        self.first_lock.acquire()
        self.second_lock.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:

        with self.first_lock:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.second_lock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:

        with self.second_lock:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()


class Foo:
    def __init__(self):
        self.first_event = threading.Event()
        self.second_event = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_event.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_event.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_event.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_event.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

# @lc code=end
