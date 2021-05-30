"""
class ListNode: def __init__(self, value): self.value = value self.next = None

    def __lt__(self, other):
        return self.value < other.value



>>> from heapq import heappush heap = [] heappush(heap,(0,{"k":0}))
>>> heappush(heap,(0,{"k":1})) Traceback (most recent call last): File
>>> "<stdin>", line 1, in <module> TypeError: '<' not supported between
>>> instances of 'dict' and 'dict'


From the heapq docs section on Priority Queue Implementation Notes:

A solution to the first two challenges is to store entries as 3-element list
including the priority, an entry count, and the task. The entry count serves as
a tie-breaker so that two tasks with the same priority are returned in the order
they were added.

A barebones interpretation of that:

from heapq import heappush ecount = 0 heap = []

    for priority, task in (
        (0, {"k":0}),
        (0, {"k":0}),
    ):
    heappush(heap, (priority, ecount, task))
    ecount += 1

Result:

>>> heap [(0, 0, {'k': 0}), (0, 1, {'k': 0})]

    (You can also do this with enumerate().)

To inject a bit of opinion into things:

Why is this happening? What is the underlying reason that such conflict is not
resolved, giving that heapq is a really old library?

Not really sure, but the fact of the matter is that you can't logically compare
two dict less than/greater than.

Independent of heapq, the comparison (0,{"k":0}) > (0,{"k":1}) will (rightfully
so) raise TypeError. An emphasis of heapq is that operations should be
deterministic: the tie-break should not be random, and it's up to you to
situationally determine how to handle that.


"""
