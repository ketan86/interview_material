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
def find_min(g, source, destination):
    result = -1
    distances = [0] * g.vertices
    # store distances from each vertex and keep incrementing based on
    # the previous vertex.
    # for ex,
    #          0
    #         / \
    #        1   2
    #       /
    #      3
    # [0, 0 ,0, 0]
    # enqueue 0 to queue and distance remains 0,
    # dequeue 0 and enqueue 1 and 2 to queue and set distance
    #               to 0(parent distanace from source) + 1 = 1
    # dequeue 1 and enqueue 3 to queue and set distance to
    # 1(parent distanace from source) + 1 = 2
    # while dequeing, if vertex is a destination, send the vertex distance.

    visited = [False] * g.vertices
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True

    while queue:
        vertex = queue.dequeue()
        adjacent = g.array[vertex].get_head()
        # if vertex value is destination, return the vertex distance from the
        # source
        if vertex == destination:
            return distances[vertex]
        while adjacent:
            if not visited[adjacent.data]:
                queue.enqueue(adjacent.data)
                visited[adjacent.data] = True
                # calculate the distance for all childs the parent
                distances[adjacent.data] = distances[vertex] + 1
            adjacent = adjacent.next_element
    return result


g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.print_graph()
print(find_min(g, 1, 6))
print(find_min(g, 2, 6))
print(find_min(g, 2, 5))
