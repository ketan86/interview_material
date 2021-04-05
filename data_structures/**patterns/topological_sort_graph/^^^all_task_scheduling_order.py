"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some
prerequisite tasks which need to be completed before it can be scheduled.
Given the number of tasks and a list of prerequisite pairs, write a method
to print all possible ordering of tasks meeting all prerequisites.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.
Example 2:

Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output: 
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all 
prerequisites.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: 
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]
"""
# pylint: skip-file
from collections import deque


def print_orders(tasks, prerequisites):
    schedule = []

    # initialize in-degree and graph.
    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    # build graph
    for prerequisite in prerequisites:
        dependency, dependent = prerequisite
        in_degree[dependent] += 1
        graph[dependency].append(dependent)

    # find all sources with in-degree 0
    task_queue = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            task_queue.append(key)

    _print_all_orders(graph, in_degree, task_queue, schedule)


def _print_all_orders(graph, in_degree, task_queue, schedule):
    # if task queue is not empty, iterate over all tasks with in-degree 0.
    if task_queue:
        for task in task_queue:
            # add task to schedule and expolore child in put them in a
            # separate queue.
            schedule.append(task)

            new_task_queue = deque(task_queue)
            new_task_queue.remove(task)
            for sub_task in graph[task]:
                in_degree[sub_task] -= 1
                if in_degree[sub_task] == 0:
                    new_task_queue.append(sub_task)
            # explore all child of new queue.
            _print_all_orders(graph, in_degree, new_task_queue, schedule)

            # one all child are explored, remove the current task from the
            # schedule and increase subtask in degree by 1.
            schedule.remove(task)
            for sub_task in graph[task]:
                in_degree[sub_task] += 1

    # when len of the schedule == in_degree length, print schedules.
    if len(schedule) == len(in_degree):
        print(schedule)


def main():
    # print("Task Orders: ")
    # print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[0, 1], [0, 2], [1, 3], [2, 3]])

    # print("Task Orders: ")
    # print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    # print("Task Orders: ")
    # print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
