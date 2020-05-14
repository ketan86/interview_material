
# pylint: skip-file
from graph import Graph

# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}


"""
This algorithm detects cycles in both directed and undirected graphs. There are
subtle different in both kinds of graphs when it comes to detecting a cycle.

directed graph:
    - self loop is considered cycle
    - backedge to parent is considered a cycle.
"""


def detect_cycle_undirected(g):
    """
    undirected graph : 
        - self loop is considered cycle
        - backedge to parent from the node is not considered cycle

    """
    # in undirected graph, if node is visited and not a parent node, cycle
    # is found.

    # initialize all the nodes to not visited
    visited = [False] * g.vertices
    # graph can have nodes that are detached but may still contain the cycle.
    # for ex, 0->1->2   3->4->5->4 - one graph but detached.
    # we start from each node to detect if there is a cycle or not.
    for i in range(g.vertices):
        # we only visit the node if it is not visited from any other previous
        # nodes cycle detection.
        if not visited[i]:
            if _has_cycle_undirected(g, i, visited, -1):
                return True
    return False


def _has_cycle_undirected(g, node, visited, parent):
    # mark node visited
    visited[node] = True
    # get the head of the node.
    adjacent = g.array[node].get_head()
    # loop over the nodes
    while adjacent:
        # if node is not visited, recursively check for cycle
        if not visited[adjacent.data]:
            if _has_cycle_undirected(g, adjacent.data, visited, node):
                return True
        else:
            # if node is visited but the adjacent node is not a parent node,
            # cycle is found.
            #          0
            #         / \
            #        1   2
            #       /   <-- this is not a cycle where node(1), adjacent node(0)
            #      0        is a parent of node(1).
            if adjacent.data != parent:
                return True
        adjacent = adjacent.next_element
    return False


def detect_cycle_directed(g):
    """
    directed graph:
        - self loop is considered cycle
        - backedge to parent is considered a cycle.
    """
    # initialize all the nodes to not visited to start with
    visited = [False] * g.vertices

    # graph can have nodes that are detached but may still contain the cycle.
    # for ex, 0->1->2   3->4->5->4 - one graph but detached.
    # we start from each node to detect if there is a cycle or not.
    for i in range(g.vertices):
        # we only visit the node if it is not visited from any other previous
        # nodes cycle detection.
        if not visited[i]:
            if _has_cycle_directed(g, i, visited):
                return True
    return False


def _has_cycle_directed(g, node, visited):
    # mark node visited
    visited[node] = True
    # get the head of the node.
    adjacent = g.array[node].get_head()
    # loop over the nodes
    while adjacent:
        # if node is visited, return 0
        if visited[adjacent.data]:
            return True
        # recursively check for cycle
        if _has_cycle_directed(g, adjacent.data, visited):
            return True
        adjacent = adjacent.next_element
    return False


# g = Graph(5)
# g.add_edge(0, 1)
# g.add_edge(1, 0)
# g.add_edge(0, 2)
# g.add_edge(2, 0)
# g.add_edge(1, 2)
# g.add_edge(2, 1)
# g.print_graph()
# print(detect_cycle_undirected(g))


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 0)
# g.add_edge(0, 2)
g.print_graph()
print(detect_cycle_undirected(g))
print(detect_cycle_directed(g))


# g = Graph(5)
# g.add_edge(0, 1)
# # g.add_edge(1, 2)
# g.add_edge(2, 1)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
# g.add_edge(4, 2)
# g.print_graph()
# print(detect_cycle_undirected(g))


# g = Graph(4)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(0, 3)
# g.add_edge(1, 0)
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(2, 0)
# g.add_edge(2, 1)
# g.add_edge(2, 3)
# g.add_edge(3, 0)
# g.add_edge(3, 1)
# g.add_edge(3, 2)
# g.print_graph()
# print(detect_cycle_undirected(g))


# g = Graph(5)
# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(1, 0)
# g.add_edge(0, 2)
# g.add_edge(2, 3)
# g.add_edge(2, 4)
# g.add_edge(3, 4)
# g.print_graph()
# print(detect_cycle_undirected(g))


# g = Graph(5)
# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.print_graph()
# print(detect_cycle_undirected(g))


# g = Graph(5)
# g.add_edge(0, 1)
# g.add_edge(1, 0)
# g.add_edge(2, 3)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
# g.add_edge(4, 2)
# g.print_graph()
# print(detect_cycle_undirected(g))
