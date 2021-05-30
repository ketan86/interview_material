"""
given a list of coursework. find the mid point from the course work completion.
there are prerequisites that you have to complete before some subjects...
eg:
[
['A', 'B', 'D']
['A', 'C', 'E']
['D', 'F']
['D', 'E']
]

the above list shows the subjects and its prerequisites.
D has A,B as its prerequisites
B has A as its prerequisite..
solution ->

odd number of elements  :  [A,B,C,D,E] -> C is the mid point
even number of elements :
    take the lower index -> [A,B,C,D,E,F] -> C is the mid point
"""
from collections import deque, defaultdict


def find_course_mid(dependencies):

    # courses result list
    courses = []

    # initialize graph and in_degree map
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # set in_degree for all courses to 0
    for course_dep_list in dependencies:
        for course in course_dep_list:
            in_degree[course] = 0

    # build graph and in_degree map
    for course_dep_list in dependencies:
        for i in range(1, len(course_dep_list)):
            dependent, dependency = course_dep_list[i-1], course_dep_list[i]
            graph[dependent].append(dependency)
            in_degree[dependency] += 1

    # find courses without any dependencies
    sources = deque()
    for k, v in in_degree.items():
        if v == 0:
            sources.append(k)

    # iterate over the sources
    while sources:
        course = sources.popleft()
        courses.append(course)
        for c in graph[course]:
            in_degree[c] -= 1
            if in_degree[c] == 0:
                sources.append(c)

    # find mid
    if len(courses) % 2 == 0:
        return courses[(len(courses) // 2) - 1]

    return courses[len(courses) // 2]


dependencies = [
    ['A', 'B', 'D'],
    ['A', 'C', 'E'],
    # ['D', 'F'],
    ['D', 'E']
]

print(find_course_mid(dependencies))
