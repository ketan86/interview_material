"""
Bloom filter is a probabilistic data structure used for searching. It
guaranties that the answer is true if key is not present but does not
guaranty that the answer is true when key is present. In the later
case, it could be or it could not be and requires a check on the storage.
"""

"""
Usages:
    1. facebook to find if userid is already taken or not ? 
    2. cache exist or not
    3. packet routing
    4. database query
"""

#  pylint: skip-file


class BloomFilter:
    def __init__(self, size=64):
        # size the bloom filter in bits
        self._size = size
        # variable to store the size of the bits
        self._storage = 0

    def _get_index(self, key):
        """
        Note: Using more hash functions reduces the change of false positive
        because there will be more than one bit in the decision of the search.
        """
        # return the index of the key within the bloom filter size bits.
        return hash(key) % self._size

    def insert(self, key):
        # find the index of the key.
        index = self._get_index(key)
        # set the bit at the index to 1 to mark that key presence.
        self._storage = self._storage | (1 << index)

    def search(self, key):
        # find the index of the key.
        index = self._get_index(key)
        # check if bit at the index is set to 1 or not. if it is set to 1,
        # we are not 100 % sure if key is present so check in the storage
        # must be performed.
        if self._storage & (1 << index):
            # NOTE: check if key is really present in the storage before
            # returning the true.
            return True
        else:
            # we are 100 % sure that the key is not present.
            return False


bf = BloomFilter()
bf.insert('ketan')
bf.insert('patel')
print(bf.search('patel'))
