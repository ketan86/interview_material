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
    # use stack for dfs
    stack = MyStack()
    # add source to stack
    stack.push(source)
    # mark all nodes non visited to start with
    visited = [False] * g.vertices
    # mark source visited
    visited[source] = True

    while not stack.is_empty():
        # pop vertex
        vertex = stack.pop()
        # add it to result
        result += str(vertex)
        # find the head of the vertext
        node = g.array[vertex].get_head()
        while node:
            # if current node is not visited, push it to stack and mark visited.
            if not visited[node.data]:
                stack.push(node.data)
                visited[node.data] = True
            # go to next ll node
            node = node.next_element
    # return result
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
