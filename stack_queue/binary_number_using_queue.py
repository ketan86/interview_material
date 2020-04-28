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
    """
    The logic here is that, number n+1 is a left shift of n and n+2 is an
    AND with 1.
    for ex,
    2 -> 1 << 1 = 2
    3 -> 2(10) & 1 = 3
    """
    result = []
    # use queue to add newly created numbers
    queue = deque()
    # add 1 to queue to start.
    queue.append(1)
    for i in range(number):
        # pop left element and append "0" and "1" to form 2 and 3
        result.append(str(queue.popleft()))
        m = result[i] + "0"
        n = result[i] + "1"
        # append 2 and 3 to queue.
        queue.append(m)
        queue.append(n)
    return result


print(findBin(10))
