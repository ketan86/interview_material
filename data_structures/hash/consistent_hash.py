"""Consistent Hashing Algorithm."""


class HashEntry:

    def __init__(self, key, val):
        self.key = key
        self.val = val


class Node:
    def __init__(self, id):
        self.id = id


class ConsistentHashRing:

    def __init__(self, size=10):
        self.size = size
        self._nodes = {}
        self._ring = [None] * self.size

    def hash(self, id):
        return hash(id) % self.size

    def add_node(self):
        new_node = Node(len(self.nodes) + 1)
        self.nodes[new_node] = self.hash(new_node.id)
