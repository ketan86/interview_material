"""
Topological Sort of a directed graph (a graph with unidirectional edges)
is a linear ordering of its vertices such that for every directed edge
(U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:

Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0

Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
Output: Following are all valid topological sorts for the given graph:
1) 4, 2, 3, 0, 1
2) 4, 3, 2, 0, 1
3) 4, 3, 2, 1, 0
4) 4, 2, 3, 1, 0
5) 4, 2, 0, 3, 1

Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
Output: Following are all valid topological sorts for the given graph:
1) 5, 6, 3, 4, 0, 1, 2
2) 6, 5, 3, 4, 0, 1, 2
3) 5, 6, 4, 3, 0, 2, 1
4) 6, 5, 4, 3, 0, 1, 2
5) 5, 6, 3, 4, 0, 2, 1
6) 5, 6, 3, 4, 1, 2, 0

There are other valid topological ordering of the graph too.
"""

# pylint: skip-file
from collections import deque


def topological_sort(vertices, edges):
    """
    STEPS:
        1. initialize the graph {source:[destinations]} and in_degree
           {source: incoming_edges_count} map to hold the data. 
        2. iterate over the edges and build the graph and in_degree maps.
        3. use queue and add all sources where in_degree is 0. 
        4. process queue and keep adding vertex to result. when in_degree
           of the vertext becomes 0, add that to a source. 
        5. if result array matches the size of the vertices (no cycle), 
           we have iterated all the vertices or else return []
    """
    result = []
    if vertices < 0:
        return result

    # initialize the graph
    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    # build the graph
    for edge in edges:
        parent, child = edge
        graph[parent].append(child)
        in_degree[child] += 1

    # find all sources with 0 in degree
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # for each source, add it to result, traverse through all the
    # child nodes and reduce the in-degree count, when in degree count becomes
    # 0, add it to sources for traversal.
    while sources:
        vertex = sources.popleft()
        result.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            # if there is a cycle, in_degree of child will not set to 0,
            # hence, will not have sources to iterate over and exit.
            if in_degree[child] == 0:
                sources.append(child)

    # check for cycle
    if len(result) != vertices:
        return []

    return result


def main():
    print("Topological sort: " +
          str(topological_sort(5, [[3, 2], [3, 0], [2, 0], [2, 1], [1, 3], [4, 3]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
