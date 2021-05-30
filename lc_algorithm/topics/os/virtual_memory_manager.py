
class MemoryAllocationError(Exception):
    """Raised when memory can not be allocated"""

class MemoryChunk:
    """Minimum contiguous memory chunk unit"""
    def __init__(self, id):
        """Constructor: `MemoryChunk`

        :param int id: A chunk id representing the memory address.
        """
        self.id = id
        # Whether the memory is available at current address or not
        self.available = True
        # A pointer to a next memory location
        self.next = None

    def __repr__(self):
        """Represents the MemoryChunk

        :return: A memory chunk representation.
        """
        return f'<MemoryChunk: id={self.id} available={self.available}, next={self.next}>'

class MemoryBlock:
    """MemoryBlock to store contiguous memory chunks"""
    def __init__(self, id, chunk_size):
        """Constructor: `MemoryBlock`

        :param int id: A memory block id.
        :param int chunk_size: A number of chunks per block.
        """
        self.chunk_size = chunk_size
        self.id = id
        # Store all chunks
        self.chunks = []
        for i in range(self.chunk_size):
            self.chunks.append(MemoryChunk(i))
        # Whether the memory block is free or not.
        self.free = True

    def __iter__(self):
        """An iterator over the memory chunks.

        :return: An iterator.
        :rtype: Iterator
        """
        return iter(self.chunks)

    def __repr__(self):
        """Represents the MemoryBlock

        :return: A memory block representation.
        """
        return '<Chunks: id={self.id} {}>'.format(chunk for chunk in self.chunks)

class MemoryManager:
    """MemoryManager that allocates and deallocates memory"""

    def __init__(self, block_size, chunk_size):
        """Constructor: `MemoryBlock`

        :param int block_size: A memory block size.
        :param int chunk_size: A memory chunk size.
        """
        self.block_size = block_size
        self.chunk_size = chunk_size
        # Total buffer size
        self.buffer_size = self.block_size * self.chunk_size
        # Remaining buffer size
        self.remaining_buffer_size = self.buffer_size
        # Store memory addresses
        self.m_addresses = []
        # Add memory blocks
        for i in range(self.block_size):
            self.m_addresses.append(MemoryBlock(i, self.chunk_size))


    def allocate(self, size):
        # If requested memory size is not available, raise 
        # MemoryAllocationError error.
        if size > self.remaining_buffer_size:
            raise MemoryAllocationError('Not enough memory to allocate')
        else:
            # Iterate over all the block and chunks and start allocating
            non_allocated_size = size
            last_chunk = None
            first_chunk = None
            for block in self.m_addresses:
                if block.free:
                    for chunk in block:
                        if non_allocated_size == 0:
                            return first_chunk
                        if chunk.available:
                            if not last_chunk:
                                first_chunk = chunk
                            chunk.available = False
                            self.remaining_buffer_size -= 1
                            non_allocated_size -= 1
                            if last_chunk:
                                last_chunk.next = chunk
                            last_chunk = chunk

            return first_chunk

    def free(self, address):
        """Free memory starting from the location.

        :param MemoryChunk address: A memory chunk address.
        """
        prev_chunk = None
        while address:
            address.available = True
            self.remaining_buffer_size += 1
            prev_chunk = address
            address = address.next
            prev_chunk.next = None


if __name__ == '__main__':
    mm = MemoryManager(block_size=3, chunk_size=4)
    address = mm.allocate(10)
    mm.free(address)
    address1 = mm.allocate(2)
    address2 = mm.allocate(3)
    mm.free(address1)
    mm.free(address2)
