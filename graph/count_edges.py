"""
You have to implement the num_edges() function which takes an undirected
graph and computes the total number of unique bidirectional edges.
An illustration is also provided for your understanding.

Input #
An undirected graph.

Output #
Returns the number of unique edges in the graph.

Sample Input #
graph = {
    0 - 2
    0 - 5
    2 - 3
    2 - 4
    5 - 3
    5 - 6
    3 - 6
    6 - 7
    6 - 8
    6 - 4
    7 - 8
}
Sample Output #
11
"""
# pylint: skip-file

from graph import Graph
from graph import MyQueue
from graph import MyStack
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}


def num_edges_undirected(g):
    edges = 0
    # go over all the vertices
    for i in range(g.vertices):
        # get the head of the node
        node = g.array[i].get_head()
        # until the end of the link list, count all edges
        while node:
            edges += 1
            node = node.next_element
    # due to bidirectional edges, each node is visited in reversed.
    return edges // 2

# directed graph edges.


def num_edges_directed(g):
    edges = 0
    for i in range(g.vertices):
        node = g.array[i].get_head()
        while node:
            edges += 1
            node = node.next_element
    return edges


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.print_graph()
print(num_edges_directed(g))


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(1, 4)
g.add_edge(3, 2)
g.add_edge(4, 3)
g.print_graph()
print(num_edges_directed(g))


g = Graph(9)
g.add_edge(0, 2)
g.add_edge(0, 5)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(5, 3)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.add_edge(6, 7)
g.add_edge(6, 8)
g.add_edge(6, 4)
g.add_edge(7, 8)

g.add_edge(2, 0)
g.add_edge(5, 0)
g.add_edge(3, 2)
g.add_edge(4, 2)
g.add_edge(3, 5)
g.add_edge(6, 5)
g.add_edge(6, 3)
g.add_edge(7, 6)
g.add_edge(8, 6)
g.add_edge(4, 6)
g.add_edge(8, 7)


g2 = Graph(7)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(3, 4)
g2.add_edge(3, 5)
g2.add_edge(2, 5)
g2.add_edge(2, 4)
g2.add_edge(4, 6)
g2.add_edge(4, 5)
g2.add_edge(6, 5)

g2.add_edge(2, 1)
g2.add_edge(3, 1)
g2.add_edge(4, 3)
g2.add_edge(5, 3)
g2.add_edge(5, 2)
g2.add_edge(4, 2)
g2.add_edge(6, 4)
g2.add_edge(5, 4)
g2.add_edge(5, 6)

print(num_edges_undirected(g))

print(num_edges_undirected(g2))
