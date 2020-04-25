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
# Depth First Traversal of Graph "g" from source vertex


def dfs_traversal(g, source):
    result = ''
    stack = MyStack()
    stack.push(source)
    visited = [False] * g.vertices
    visited[source] = True

    while not stack.is_empty():
        vertex = stack.pop()
        node = g.array[vertex].get_head()
        result += str(vertex)
        while node:
            if not visited[node.data]:
                stack.push(node.data)
                visited[node.data] = True
            node = node.next_element
    return result


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.print_graph()
print(dfs_traversal(g, 0))

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 0)
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(1, 6)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 0)
g.add_edge(3, 1)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.add_edge(4, 3)
g.add_edge(4, 6)
g.add_edge(4, 2)
g.add_edge(5, 1)
g.add_edge(5, 2)
g.add_edge(6, 1)
g.add_edge(6, 4)
g.print_graph()
print(dfs_traversal(g, 0))
