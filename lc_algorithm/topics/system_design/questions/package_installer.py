"""
Given a dependency graph and a package name, return all direct and indirect
dependencies of the package in a list.

Input:
package: "a"
dep_graph: {
  a: ['b','c'],
  b: ['d'],
}

Output: ['b','c','d']

Note that the dependency graph can have a cycle.
"""
from collections import deque, defaultdict
def install_package(package, dep_graph):
    """
    NOTE: This can be solved by doing order level traversal from the package
    node and pushing items in reverse order.

                      B -- D
                    /
                  A
                    \
                      C

                  E -- F
    """
    dep_path = deque()

    if package not in dep_graph:
        return dep_path

    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # build graph and in_degree for the packages that are involved in the
    # installation/un-installation path.
    stack = [package]
    while stack:
        p = stack.pop()
        if p not in in_degree:
            in_degree[p] = 0
        if p not in graph:
            graph[p] = []
        if p in dep_graph:
            for child in dep_graph[p]:
                in_degree[child] += 1
                graph[p].append(child)
                stack.append(child)

    sources = deque()
    for k,v in in_degree.items():
        if v == 0:
            sources.append(k)

    while sources:
        parent = sources.popleft()
        dep_path.appendleft(parent)
        for child in graph[parent]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(dep_path) != len(graph):
        return []

    return list(dep_path)

def uninstall_package(package, dep_graph):
    return list(
        reversed(install_package(package, dep_graph)))

print(install_package('A', {
  'A': ['B','C'],
  'B': ['D'],
  'E' : ['F']
}))

print(uninstall_package('A', {
  'A': ['B','C'],
  'B': ['D'],
  'E' : ['F']
}))