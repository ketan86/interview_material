"""
The next section will tackle the tree data structure. For now, here’s the
basic difference between a graph and a tree. A graph can only be a tree
under two conditions:

There are no cycles.
The graph is connected.

A graph is connected when there is a path between every pair of vertices.
In a connected graph, there are no unreachable vertices. Each vertex must
be able to reach every other vertex through either a direct edge or through
a graph traversal.

You have to implement is_tree() function which will take a graph as an input
and find out if it is a tree.

Input #
An undirected graph.

Output #
Returns True if the given graph is a tree. Otherwise, it returns False.

Sample Input #
graph = {
    0 - 1
    0 - 2
    0 - 3
    3 - 4
}
Sample Output #
True

For a directed graph:

Find the vertex with only outgoing edges (if there is more than one or no such
vertex, fail).
Do a BFS or DFS from that vertex. If you encounter an already visited vertex,
it's not a tree.
If you're done and there are unexplored vertices, it's not a tree - the graph
is not connected.

Otherwise, it's a tree.
To check for a binary tree, additionally check if each vertex has at most 2
outgoing edges.

For an undirected graph:
Check for a cycle with a simple depth-first search (starting from any vertex)
- "If an unexplored edge leads to a node visited before, then the graph
    contains a cycle." If there's a cycle, it's not a tree.
If the above process leaves some vertices unexplored, it's not a tree,
because it's not connected.

Otherwise, it's a tree.
To check for a binary tree, additionally check that all vertices have
1-3 edges (one to the parent and 2 to the children).

Checking for the root, i.e. whether one vertex contains 1-2 edges, is not
necessary as there has to be vertices with 1-2 edges in an acyclic connected
undirected graph.
Note that identifying the root is not generically possible (it may be possible
in special cases) as, in many undirected graphs, more than one of the nodes
can be made the root if we were to make it a binary tree.
"""

# pylint: skip-file
from graph import Graph


def is_tree(g): # <-- undirected graph
    # define all nodes to not visited
    visited = [False] * g.vertices
    # if there are cycles, it is not a tree.
    if _has_cycle(g, 0, visited, -1):
        return False
    # if all nodes are not visited, it's not a tree.
    return all(visited)


def _has_cycle(g, node, visited, parent):
    # mark node visited
    visited[node] = True
    # get head and traverse.
    adjacent = g.array[node].get_head()
    while adjacent:
        # if not visited, check for cycle
        if not visited[adjacent.data]:
            if _has_cycle(g, adjacent.data, visited, node):
                return True
        # if visited and not the parent, If node is parent, we can't
        # consider it a loop.
        elif adjacent.data != parent:
            return True
        adjacent = adjacent.next_element
    return False


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 4)
g.print_graph()
print(is_tree(g))


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)
g.print_graph()
print(is_tree(g))
