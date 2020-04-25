"""
Implement Hash Table.
"""
# pylint: skip-file


class HashEntry:
    """
    Hash Entry contains key, data and pointer to next node.
    """

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class HashTable:
    """
    Hash Table contains a list of indexes mapped to a given key.
    """

    def __init__(self, slots=10):
        self.slots = slots
        self.size = 0
        self.bucket = [None] * self.slots
        self.threshold = 0.6

    def __len__(self):
        return self.size

    def is_emptry(self):
        return len(self) == 0

    def get_index(self, key):
        return hash(key) % self.slots

    def resize(self):
        self.slots *= 2
        new_bucket = [None] * self.slots
        for i in self.bucket:
            head = i
            while head:
                new_index = self.get_index(head.key)
                if not new_bucket[new_index]:
                    new_bucket[new_index] = HashEntry(head.key, head.data)
                else:
                    # attach to tail
                    node = new_bucket[new_index]
                    while node:
                        if node.key == head.key:
                            node.value = head.value
                        elif not node.next:
                            node.next = HashEntry(head.key, head.value)
                        else:
                            node = node.next
                head = head.next
        self.bucket = new_bucket

    def insert(self, key, value):
        index = self.get_index(key)
        if not self.bucket[index]:
            self.bucket[index] = HashEntry(key, value)
            self.size += 1
        else:
            head = self.bucket[index]
            while head:
                if head.key == key:
                    head.value = value
                    break
                elif not head.next:
                    head.next = HashEntry(key, value)
                    self.size += 1
                    break
                head = head.next

        load_factor = float(self.size) / float(self.slots)
        if load_factor >= self.threshold:
            self.resize()

    def search(self, key):
        index = self.get_index(key)
        head = self.bucket[index]
        while head:
            if head.key == key:
                return True
            head = head.next
        return False

    def delete(self, key):
        index = self.get_index(key)
        head = self.bucket[index]
        prev = head
        while head:
            if head.key == key:
                prev.next = head.next
                self.size -= 1
                return
            prev = head
            head = head.next


ht = HashTable()
print(ht.slots)
# Current capacity
ht.insert(2, "London")
# Collides with (2, "London") - Added next to it at the same index
ht.insert(12, "Moscow")
ht.insert(7, "Paris")
print(ht.size)
# New capacity
ht.delete(12)
ht.delete(12)
print(ht.size)
print(ht.search(12))
