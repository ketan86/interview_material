"""


Given a set of relationship between parent and child , create two lists
where one presents children with one parent while another one where children
with no known parents. 

[[1,3][2,3][3,4][4,5][6,5]] -> {4} & {1,2,6}
"""
from collections import deque
import heapq
from collections import defaultdict


def find_parents(relations):
    in_degree = defaultdict(int)

    for relation in relations:
        parent, child = relation
        if parent not in in_degree:
            in_degree[parent] = 0
        in_degree[child] += 1

    # {1-> 0, 2-> 0, 3 ->2, 4->1, 5->2, 6 -> 0}

    no_parent = []
    one_parent = []
    for child in in_degree:
        if in_degree[child] == 0:
            no_parent.append(child)
        elif in_degree[child] == 1:
            one_parent.append(child)

    return one_parent, no_parent


print(find_parents([[1, 3], [2, 3], [3, 4], [4, 5], [6, 5]]))


"""

Suppose we have some input data describing a graph of relationships between
parents and children over multiple generations. The data is formatted as a list
of (parent, child) pairs, where each individual is assigned a unique integer
identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

     14  13
     |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11
parent_child_pairs_1 = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),(4, 8),
(4, 9), (9, 11), (14, 4), (13, 12), (12, 9)]

Write a function that takes the graph, as well as two of the individuals in our
dataset, as its inputs and returns true if and only if they share at least one
ancestor.

Sample input and output:

has_common_ancestor(parent_child_pairs_1, 3, 8) => false
has_common_ancestor(parent_child_pairs_1, 5, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 8) => true
has_common_ancestor(parent_child_pairs_1, 6, 9) => true
has_common_ancestor(parent_child_pairs_1, 1, 3) => false
has_common_ancestor(parent_child_pairs_1, 3, 1) => false
has_common_ancestor(parent_child_pairs_1, 7, 11) => true
has_common_ancestor(parent_child_pairs_1, 6, 5) => true
has_common_ancestor(parent_child_pairs_1, 5, 6) => true

Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
 \ /    / \
  3    6   7
   \        \
    4        8
parent_child_pairs_2 = [(11, 10), (11, 12), (2, 3), (10, 2), (10, 5), (1, 3),
(3, 4), (5, 6), (5, 7), (7, 8),]

has_common_ancestor(parent_child_pairs_2, 4, 12) => true
has_common_ancestor(parent_child_pairs_2, 1, 6) => false
has_common_ancestor(parent_child_pairs_2, 1, 12) => false

n: number of pairs in the input
"""


def has_common_ancestor(relations, a, b):
    graph = defaultdict(list)

    # form child to parent graph and dfs upward to find all parents
    for relation in relations:
        parent, child = relation
        graph[child].append(parent)

    a_parents = set()
    b_parents = set()

    dfs(graph, a, a_parents)
    dfs(graph, b, b_parents)

    return len(a_parents.intersection(b_parents)) != 0


def dfs(graph, node, node_parents):
    if not node or node not in graph:
        return

    # iterate over all parents and keep going up
    for n in graph[node]:
        node_parents.add(n)
        dfs(graph, n, node_parents)


# def dfs(graph, node):
#     ancestors = set()
#     stack = [node]
#     while stack:
#         node = stack.pop()
#         parents = graph[node]
#         for parent in parents:
#             ancestors.add(parent)
#             stack.append(parent)
#     return ancestors

pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
         (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)]

print(has_common_ancestor(pairs, 3, 8))
print(has_common_ancestor(pairs, 5, 8))
print(has_common_ancestor(pairs, 6, 8))
print(has_common_ancestor(pairs, 1, 3))


"""
Find furthest parent node. Use BFS instead of dfs to find the furthest node.
"""


def find_furthest_parent(relations, a):
    graph = defaultdict(list)

    # form child to parent graph and dfs upward to find all parents
    for relation in relations:
        parent, child = relation
        graph[child].append(parent)

    return bfs(graph, a)


def bfs(graph, node):
    furthest = -1
    queue = deque()
    queue.append(node)

    while queue:
        n = queue.popleft()
        if n in graph:
            for c in graph[n]:
                furthest = c
                queue.append(c)

    return furthest


pairs = [(11, 10), (11, 12), (2, 3), (10, 2), (10, 5), (1, 3),
         (3, 4), (5, 6), (5, 7), (7, 8), ]

print(find_furthest_parent(pairs, 11))
