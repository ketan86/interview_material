"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.



Follow up:
Could you do both operations in O(1) time complexity?



Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
# pylint: skip-file
import time
import heapq
from collections import defaultdict, OrderedDict


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.freq_map = {}
        self.size = 0

    # def get(self, key):
    #     if key in self.hash_map:
    #         node = self.hash_map[key]
    #         node.freq += 1
    #         self.adjust(node)
    #         return node.data
    #     return -1

    def put(self, key, data):
        self._resize()
        if key in self.hash_map:
            node = self.hash_map[key]
            node.freq += 1
            self.adjust(node)
        else:
            self.hash_map[key] = self.insert(data)

    # def adjust(self, node):
    #     if node == self.head:
    #         return

    #     while node and node.prev and node.prev.freq <= node.freq:
    #         if node == self.tail:
    #             self.tail = node.prev
    #         node = self._swap(node, node.prev)

    # def _swap(self, node, prev):
    #     prev_prev = prev.prev
    #     temp = prev
    #     if prev_prev:
    #         prev_prev.next = node
    #     else:
    #         self.head = node
    #     node.prev = prev_prev
    #     next_ = node.next
    #     node.next = temp
    #     temp.prev = node
    #     temp.next = next_
    #     if next_:
    #         next_.prev = temp
    #     return node

    # def insert(self, data):
    #     if self.head is None:
    #         self.head = Node(data)
    #         self.tail = self.head
    #     else:
    #         node = Node(data)
    #         head = self.head
    #         node.next = head
    #         head.prev = node
    #         self.head = node

    #     self.size += 1
    #     return self.head

    # def _resize(self):
    #     if self.size >= self.capacity:
    #         del self.hash_map[self.tail.data]
    #         prev = self.tail.prev
    #         prev.next = None
    #         self.tail = prev
    #         self.size -= 1

    def print(self):
        # print nodes
        head = self.head
        while head:
            print(head.data, end='->')
            head = head.next


# class LFUCache:

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.cache = {}
#         self.count = defaultdict(OrderedDict)
#         self.min = 0
#         self.capacity = capacity

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self.cache:
#             return -1
#         value, count = self.cache[key]
#         del self.count[count][key]
#         if count == self.min and not self.count[count]:
#             self.min += 1
#         self.count[count+1][key] = 0
#         self.cache[key] = (value, count+1)
#         return value

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: void
#         """
#         if self.capacity <= 0:
#             return
#         if key in self.cache:
#             old_val, count = self.cache[key]
#             self.cache[key] = (value, count)
#             self.get(key)
#         elif len(self.cache) == self.capacity:
#             old_key, v = self.count[self.min].popitem(last=False)
#             del self.cache[old_key]
#             self.min = 1
#             self.cache[key] = (value, 1)
#             self.count[1][key] = 0
#         else:
#             self.min = 1
#             self.cache[key] = (value, 1)
#             self.count[1][key] = 0


# lfu = LFUCache(capacity=5)
# lfu.get(0)
# lfu.put(0, 0)
# lfu.put(2, 2)
# print(lfu.print())
# lfu.get(0)
# print(lfu.print())
# lfu.put(1, 1)
# lfu.get(0)
# lfu.get(1)
# lfu.get(2)
# print(lfu.print()
# lfu.put(2, 2)
# lfu.put(3, 3)
# lfu.put(4, 4)
# lfu.put(5, 5)
# lfu.put(6, 6)
# lfu.get(4)
# print(lfu.print())


"""
LFU using map and min heap.
"""

# c = Cache(size=2)
# c.set(1,1)
# c.set(2,2) // None
# c.get(1) // 1
# c.get(2) // 2
# c.set(3,3) // evict
# c.get(2) // -1


# integers key, value pair
# evict based on lease freq used
# set duplicate items, no-op
# same freq, lease recent used

# key -> ->head->Node(3)->node(1)<- tail
# 3(4),2(4),1(4)


class Node:
    def __init__(self, key, value, freq=0):
        self.key = key
        self.value = value
        self.freq = freq
        self.timestamp = time.time()

    def __lt__(self, other):
        # if freq of the two nodes are same, latest timestmap wins
        if self.freq == other.freq:
            return self.timestamp < other.timestamp
        else:
            return self.freq < other.freq

    def __repr__(self):
        return f'<Node={self.key}, {self.value}, {self.freq}, {self.timestamp}'


class Cache:
    def __init__(self, size):
        self.size = size
        self.map = {}  # key -> Node()
        self.min_heap = []
        """
            4 -> Node()
            [1,4 : 2,6, 3:8]
        """

    def set(self, key, value):
        # create a new node and assign to a key
        node = Node(key, value)
        self.map[key] = node

        # resize the heap
        if len(self.min_heap) == self.size:
            # replace the top element with new item (new item stays)
            least_freq_used_node = heapq.heapreplace(self.min_heap, node)
            del self.map[least_freq_used_node.key]
        else:
            heapq.heappush(self.min_heap, node)

    def get(self, key):
        if key not in self.map:
            return -1

        # update freq and heapify
        self.map[key].freq += 1

        # NOTE: All changes to heap should either be done via heapq methods
        # or heapify (if items changes) to maintain the heap invariant.
        heapq.heapify(self.min_heap)

        return self.map[key].value


c = Cache(size=2)
c.set(1, 1)
c.set(2, 2)
print(c.get(1))
print(c.get(2))
# print(c.get(1))
c.set(3, 3)
print(c.get(2))
