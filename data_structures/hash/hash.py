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
        # define the size of the hash table
        self.slots = slots
        # define a variable to hold the current size of the hash table
        self.size = 0
        # create a list to hold keys. at each index, we will store the
        # linked list root node.
        self.bucket = [None] * self.slots
        # set a threshold and when it's met, resize the hash table.
        self.threshold = 0.6

    def __len__(self):
        # return the current size of the hash table.
        return self.size

    def is_emptry(self):
        # check to see if hash table is empty
        return len(self) == 0

    def get_index(self, key):
        # find the index of the slot list by hasing the key and using
        # modulo operator.
        return hash(key) % self.slots

    def resize(self):
        # double the slot size
        self.slots *= 2
        # define a new bucket
        new_bucket = [None] * self.slots
        # loop over the bucket indexes
        for i in self.bucket:
            # get the head
            head = i
            # loop over the linked list
            while head:
                # get new index because slots are doubled.
                new_index = self.get_index(head.key)
                # if new index is not used in the bucket, set a key
                if not new_bucket[new_index]:
                    new_bucket[new_index] = HashEntry(head.key, head.data)
                else:
                    # find the tail and add new element.
                    node = new_bucket[new_index]
                    while node:
                        # if key is present, change the value
                        if node.key == head.key:
                            node.value = head.value
                        # if last node is found, set new node at the tail
                        elif not node.next:
                            node.next = HashEntry(head.key, head.value)
                        else:
                            node = node.next
                # move the head
                head = head.next

        # update the current bucket with the new bucket
        self.bucket = new_bucket

    def insert(self, key, value):
        # find the index where value of the key is going to be stored.
        index = self.get_index(key)
        # if index is available, create a node and increment the size.
        if not self.bucket[index]:
            self.bucket[index] = HashEntry(key, value)
            self.size += 1
        else:
            # if index is used, find the head
            head = self.bucket[index]
            # loop over the linked list
            while head:
                # if key is already present, replace the value and break
                if head.key == key:
                    head.value = value
                    break
                # if next element is None, create a node and increment the
                # size of the hashmap.
                elif not head.next:
                    head.next = HashEntry(key, value)
                    self.size += 1
                    break
                # move the head
                head = head.next

        # find the load factor and if it's >= threshold, resize the hash table
        load_factor = float(self.size) / float(self.slots)
        if load_factor >= self.threshold:
            self.resize()

    def search(self, key):
        # find the index of the key
        index = self.get_index(key)
        # find the head
        head = self.bucket[index]
        # loop over the linked list
        while head:
            # if key is found, return True
            if head.key == key:
                return True
            head = head.next
        # return False if not found
        return False

    def delete(self, key):
        # find the index of the key
        index = self.get_index(key)
        # find the head
        head = self.bucket[index]
        # define prev to save prev node
        prev = None
        # loop over the linked list
        while head:
            # if key is found, delete the node
            if head.key == key:
                prev.next = head.next
                # decrement the hash table size
                self.size -= 1
                return True
            # set prev
            prev = head
            # move head
            head = head.next
        return False


ht = HashTable()
print(ht.slots)
# Current capacity
ht.insert(2, "London")
# Collides with (2, "London") - Added next to it at the same index
ht.insert(12, "Moscow")
ht.insert(7, "Paris")
print(ht.size)
# New capacity
print(ht.delete(12))
print(ht.delete(12))
print(ht.size)
print(ht.search(12))
