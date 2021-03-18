"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some
prerequisite tasks which need to be completed before it can be scheduled.
Given the number of tasks and a list of prerequisite pairs, write a method
to find the ordering of tasks we should pick to finish all tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly,
task '1' needs to finish
before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2]
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The tasks have cyclic dependency, therefore they cannot be
scheduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: [0 1 4 3 2 5]
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5]
"""

# pylint: skip-file
from collections import deque


def find_order(tasks, prerequisites):
    schedule = []
    # if we find a cycle during the topological search, scheduling is not
    # possible, else yes.

    # initialize in-degree and graph
    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    # build the graph
    for prerequisite in prerequisites:
        dependency, dependent = prerequisite
        graph[dependency].append(dependent)
        in_degree[dependent] += 1

    # find tasks with in-degree 0.
    task_queue = deque()
    for task in in_degree:
        if in_degree[task] == 0:
            task_queue.append(task)

    # iterate over tasks and all dependent tasks. reduce the in-degree value
    # and when reches 0, add that task into tasks queue.
    while task_queue:
        task = task_queue.popleft()
        schedule.append(task)
        for sub_task in graph[task]:
            in_degree[sub_task] -= 1
            if in_degree[sub_task] == 0:
                task_queue.append(sub_task)

    # if all tasks are not scheduled, scheduling is not possible.
    if len(schedule) != tasks:
        return []

    return schedule


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
