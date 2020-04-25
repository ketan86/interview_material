"""
Implement a function findBin(n) which will generate binary numbers from 11
till n in the form of a string using a queue. The myQueue() and myStack()
classes are provided in all of these challenges. An illustration is also
provided for your understanding.

Input #
A positive integer nn

Output #
Returns binary numbers in the form of strings from 1 up to n

Sample Input #
n = 3
Sample Output #
result = ["1","10","11"]
"""

#pylint: skip-file
from collections import deque


def findBin(number):
    result = []
    queue = deque()
    queue.append(1)
    for i in range(number):
        result.append(str(queue.popleft()))
        m = result[i] + "0"
        n = result[i] + "1"
        queue.append(m)
        queue.append(n)
    return result


print(findBin(10))
