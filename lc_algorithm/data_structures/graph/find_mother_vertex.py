"""
You have to implement the find_mother_vertex() function which will take a
graph as an input and find out which vertex is the mother vertex in the graph.

By definition, the mother vertex is one from which all other vertices are
reachable. A graph can have multiple mother vertices, but you only need to find one.

Input #
A directed graph

Output #
Returns the value of the mother vertex if it exists. Otherwise, it returns -1

Sample Input #
graph = {
        3 -> 0 
    3 -> 1
    0 -> 1
    1 -> 2
}
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


def find_mother_vertex(g):
    for i in range(g.vertices):
        visited = dfs_traversal(g, i)
        # if all nodes are visited from the given node, that is the one of
        # the mother vertex
        if all(visited):
            return i


def dfs_traversal(g, source):
    stack = MyStack()
    stack.push(source)
    visited = [False] * g.vertices
    visited[source] = True
    while not stack.is_empty():
        vertex = stack.pop()
        node = g.array[vertex].get_head()
        while node:
            if not visited[node.data]:
                stack.push(node.data)
                visited[node.data] = True
            node = node.next_element
    return visited


g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.print_graph()
print(find_mother_vertex(g))

g = Graph(4)
g.add_edge(3, 0)
g.add_edge(3, 1)
g.add_edge(1, 2)
g.add_edge(0, 1)
g.print_graph()
print(find_mother_vertex(g))
