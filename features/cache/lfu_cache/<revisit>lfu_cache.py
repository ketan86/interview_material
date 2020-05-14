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


lfu = LFUCache(capacity=5)
lfu.get(0)
lfu.put(0, 0)
lfu.put(2, 2)
print(lfu.print())
lfu.get(0)
print(lfu.print())
lfu.put(1, 1)
lfu.get(0)
lfu.get(1)
lfu.get(2)
print(lfu.print()
lfu.put(2, 2)
lfu.put(3, 3)
lfu.put(4, 4)
lfu.put(5, 5)
lfu.put(6, 6)
lfu.get(4)
print(lfu.print())
