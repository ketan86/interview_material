"""
Problem Statement #
You have to implement the check_path() function. It takes a source and a
destination and tells us whether or not a path exists between the two
(from the source to the destination).

Input #
A graph, a source value, and a destination value.

Output #
Returns True if a path exists from the source to the destination.

Sample Input #
graph = {
        0 -> 2
    0 -> 5
    2 -> 3
    2 -> 4
    5 -> 3
    5 -> 6
    3 -> 6
    6 -> 7
    6 -> 8
    6 -> 4
    7 -> 8
}
 
source = 0
destination = 7
Sample Output #
True
"""
# pylint: skip-file

from graph import Graph, MyQueue, MyStack
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}


def check_path(g, source, destination):
    visited = [False] * g.vertices
    queue = MyQueue()
    queue.enqueue(source)
    while not queue.is_empty():
        vertex = queue.dequeue()
        node = g.array[vertex].get_head()
        while node:
            if node.data == destination:
                return True
            if not visited[node.data]:
                queue.enqueue(node.data)
                visited[node.data] = True
            node = node.next_element
    return False
# Make helper functions here


g1 = Graph(9)
g1.add_edge(0, 2)
g1.add_edge(0, 5)
g1.add_edge(2, 3)
g1.add_edge(2, 4)
g1.add_edge(5, 3)
g1.add_edge(5, 6)
g1.add_edge(3, 6)
g1.add_edge(6, 7)
g1.add_edge(6, 8)
g1.add_edge(6, 4)
g1.add_edge(7, 8)
g1.print_graph()
g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(2, 3)
g2.print_graph()


print(check_path(g1, 0, 7))
print(check_path(g2, 3, 0))
