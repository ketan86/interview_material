### Running Instruction
`python3 virtual_memory_manager.py`

### Run Test-cases
`python3 tests.py`

### Improvements
1. if contiguous memory is required, each block remaining size can be calculated to find the block that can fit the required memory.
2. In case of contiguous memory requirement, we can implement compaction algorithm to save memory with the penalty of compaction.
3. MemoryChunk level locking can be provided to make it thread-safe.
4. MemoryChunk size can be configured for custom size.
