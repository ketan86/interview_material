"""
Implement the find_min() function which will take a graph and two vertices,
A and B. The result will be the shortest path from A to B.

Remember, the shortest path will contain the minimum number of edges.

Input #
A directed graph, a vertex A and a vertex B.

Output #
Returns number of edges in the shortest path between A and B.

Sample Input #
graph = {
    0 - 1
    0 - 2
    0 - 3
    3 - 5
    5 - 4
    2 - 4
}

Vertex A = 0
Vertex B = 4

Sample Output #
2

"""
from graph import Graph, MyQueue
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}


# BFS gives the shortest path during the traversal and once visited,
# it will not be visited via longer path.
def find_min_distance(g, source, destination):
    distance = 0
    # if source and destination values are same, return
    # distance 0.
    if source == destination:
        return distance

    # use visited list to mark visited node.
    visited = [False] * g.vertices
    queue = MyQueue()
    # store node and distance from the source starting at 0
    queue.enqueue((source, distance))
    visited[source] = True

    # loop over the queue until not empty, do not use queue until __len__
    # is implemented on the queue to return the length of the queue when
    # used in a loop to check the object like here.
    # NOTE: dequeue from builtins supports __len__ so can be used like
    # queue = dequeue()
    # while queue:
    #   ...
    while not queue.is_empty():
        vertex, distance = queue.dequeue()
        adjacent = g.array[vertex].get_head()
        # if vertex is the destination node, return the current distance
        if vertex == destination:
            return distance
        while adjacent:
            if not visited[adjacent.data]:
                # increment the distance of the parent by 1 and add it to
                # adjacent node.
                queue.enqueue((adjacent.data, distance + 1))
                visited[adjacent.data] = True
            adjacent = adjacent.next_element
    return distance


g = Graph(10)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(3, 7)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(4, 7)
g.add_edge(7, 8)
# g.add_edge(8, 6)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.print_graph()

print(find_min_distance(g, 1, 6))
print(find_min_distance(g, 2, 6))
print(find_min_distance(g, 2, 6))
print(find_min_distance(g, 4, 6))
print(find_min_distance(g, 1, 8))
print(find_min_distance(g, 7, 6))
