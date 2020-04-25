
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
Detect cycle in the undirected graph.

In graph without cycle, adjacent node will not have backedge to it's ancestors.

To detect the cycle, an adjacent node 
"""


def detect_cycle(g):
    visited = [-1] * g.vertices
    for i in range(g.vertices):
        if _has_cycle(g, i, visited, -1):
            return True
    return False


def _has_cycle(g, node, visited, parent):
    visited[node] = 0
    adjacent = g.array[node].get_head()
    while adjacent:
        if visited[adjacent.data] == 0:
            return True
        if visited[adjacent.data] != 1:
            if _has_cycle(g, adjacent.data, visited, node):
                return True
        adjacent = adjacent.next_element
    visited[node] = 1
    return False


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 0)
g.add_edge(1, 2)
g.add_edge(2, 1)
g.add_edge(0, 2)
g.add_edge(2, 0)
g.print_graph()
print(detect_cycle(g))


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()
print(detect_cycle(g))


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(4, 2)
g.print_graph()
print(detect_cycle(g))


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 0)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(3, 1)
g.add_edge(3, 2)
g.print_graph()
print(detect_cycle(g))


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.print_graph()
print(detect_cycle(g))


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.print_graph()
print(detect_cycle(g))


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 0)
g.add_edge(2, 3)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(4, 2)
g.print_graph()
print(detect_cycle(g))
