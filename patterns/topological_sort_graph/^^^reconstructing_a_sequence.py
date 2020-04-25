"""
Given a sequence originalSeq and an array of sequences, write a method to
find if originalSeq can be uniquely reconstructed from the array of sequences.

Unique reconstruction means that we need to find if originalSeq is the only
sequence such that all sequences in the array are subsequences of it.

Example 1:

Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
Output: true
Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct
[1, 2, 3, 4], in other words, all the given sequences uniquely define the
order of numbers
in the 'originalSeq'.
Example 2:

Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
Output: false
Explanation: The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely
reconstruct
[1, 2, 3, 4]. There are two possible sequences we can construct from the
given sequences:
1) [1, 2, 3, 4]
2) [1, 2, 4, 3]
Example 3:

Input: originalSeq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
Output: true
Explanation: The sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely
reconstruct
[3, 1, 4, 2, 5].
"""

# pylint: skip-file
from collections import deque


def can_construct(origin_sequence, sequences):
    """
    Using the sequence, we can form a graph and perform a topological sort
    on it. During the sorting, if we find a node with 2 out_degree, there
    can't uniquely reconstruct the sequence.

    If we have only one ordering, if that matches the original sequence,
    we found the unique reconstruction.
    """
    sorted_order = []
    if len(origin_sequence) == 0:
        return False

    # initialize the graph
    in_degree = {}
    graph = {}
    for sequence in sequences:
        for num in sequence:
            in_degree[num] = 0
            graph[num] = []

    # if we dont have ordering rules for all the numbers, we wont have the
    # unique reconstruction.
    if len(origin_sequence) != len(in_degree):
        return False

    # build the graph
    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i - 1], sequence[i]
            graph[parent].append(child)
            in_degree[child] += 1

    # find all sources with in_degree 0.
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # topological sorting
    while sources:
        # if there are more than two sources, we wont have the unique
        # reconstruction.
        if len(sources) > 1:
            return False

        # if order sequence is different from the original, return false
        if origin_sequence[len(sorted_order)] != sources[0]:
            return False

        vertex = sources.popleft()
        sorted_order.append(vertex)

        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(sorted_order) == len(origin_sequence)


def main():
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
          str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
