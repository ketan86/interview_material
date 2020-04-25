"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


Question: Why Doubly Linked List ?
Answer  : Once we find the node from the map, we will not have a reference to
previous node (we will have a referent to next node) so deletion will not be
possible in singly linked list hence, we use the doubly linked list.
"""

# pylint: skip-file


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity=10):
        # capacity of cache
        self.capacity = capacity
        # hash map to store a cache key to a value (link list Node)
        self.hash_map = {}
        # head to track the newly accessed or inserted item.
        self.head = None
        # tail to delete item if cache size reaches beyond capacity
        self.tail = None
        # current size of the cache
        self.size = 0

    def put(self, key, value):
        if key not in self.hash_map:
            # check if size is over the limit. If yes, move tail to
            # prev node and detach the node.
            self._resize()
            # insert the new node to head
            node = self._insert(value)
            # set a node as value to a key
            self.hash_map[key] = node
        else:
            # access the node from a key
            node = self.hash_map[key]
            # move node to front due to access.
            self._adjust(node)

    def get(self, key):
        # if key is present in map, access the node and move node to front
        if key in self.hash_map:
            node = self.hash_map[key]
            self._adjust(node)
            # return the node value
            return node.data
        return -1

    def _adjust(self, node):

        # if node is a head node, no need to move the node to front.
        if node == self.head:
            # if current node is head node, no op.
            return

        # if node is a tail node, that node is moving to front so tail
        # must move to prev node.
        if node == self.tail:
            # if current node is tail node, set tail node to prev node.
            self.tail = node.prev

        # delete the node
        prev_node = node.prev
        next_node = node.next

        # if prev_node is none, it's a head node.
        if prev_node:
            prev_node.next = next_node
        # if next node is none, it's a tail node.
        if next_node:
            next_node.prev = prev_node

        # insert the current node to head.
        head = self.head
        node.next = head
        head.prev = node
        node.prev = None
        self.head = node

    def _resize(self):
        # if size of the link list is equal to capacity, remove the tail node.
        # also, remove the tail from hash map.
        if self.size == self.capacity:
            del self.hash_map[self.tail.data]
            prev = self.tail.prev
            self.tail.prev.next = None
            self.tail = prev
            self.size -= 1

    def _insert(self, value):
        # if head is none, set a new node to head and tail.
        # as head node move toward the end, tail node moves along with it.
        # there is no need to adjust the tail after first node is created.
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            # add a new node to head.
            head = self.head
            new_node = Node(value)
            new_node.next = head
            head.prev = new_node
            self.head = new_node
        self.size += 1

        return self.head

    def print(self):
        # print nodes
        head = self.head
        while head:
            print(head.data, end='->')
            head = head.next


lru = LRUCache(capacity=5)
print(lru.get(0))
lru.put(0, 0)
lru.put(2, 2)
print(lru.print())
print(lru.get(0))
print(lru.print())
lru.put(1, 1)
print(lru.get(1))
print(lru.get(2))
print(lru.print())
lru.put(2, 2)
lru.put(3, 3)
lru.put(4, 4)
lru.put(5, 5)
lru.put(6, 6)
print(lru.get(4))
print(lru.print())
