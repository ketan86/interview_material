from graph import Graph
from graph import MyQueue
# You can check the input graph in console tab

# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Graph => graph = Graph(vertices)
# Create LinkedList => link_list = LinkedList()
# Functions of LinkedList => insert_at_head(Node), is_empty(), delete(),
#                            delete_at_head(list), search(), print_list()
# class Node => data, next_element
# Breadth First Traversal of Graph g from source vertex


def bfs_traversal(g, source):
    # result array
    result = ''
    # use queue to store the nodes
    queue = MyQueue()
    # add source to queue
    queue.enqueue(source)
    # mark all verticies non visited to start with.
    visited = [False] * g.vertices
    # mark source node visited.
    visited[source] = True

    # until queue is empty, iterate
    while not queue.is_empty():
        # get the vertex from the queue
        vertex = queue.dequeue()
        # add it to result
        result += str(vertex)
        # get the linked list head
        node = g.array[vertex].get_head()

        # visit each linked list node
        while node:
            # if not visited, visit and add edges to queue and mark is visited.
            if not visited[node.data]:
                queue.enqueue(node.data)
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
print(bfs_traversal(g, 0))


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
print(bfs_traversal(g, 0))
