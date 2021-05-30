"""
We are working on a security system for a badged-access room in our company's
building.

We want to find employees who badged into our secured room unusually often. We
have an unordered list of names and entry times over a single day. Access times
are given as numbers up to four digits in length using 24-hour time, such as
"800" or "2250".

Write a function that finds anyone who badged into the room three or more times
in a one-hour period, and returns each time that they badged in during that
period. (If there are multiple one-hour periods where this was true, just return
the first one.)

badge_times = [
    ["Paul", 1355],
    ["Jennifer", 1910],
    ["John", 830],
    ["Paul", 1315],
    ["John", 1615],
    ["John", 1640],
    ["John", 835],
    ["Paul", 1405],
    ["John", 855],
    ["John", 930],
    ["John", 915],
    ["John", 730],
    ["Jennifer", 1335],
    ["Jennifer", 730],
    ["John", 1630],
]

Expected output ( in any order)
John: 830 835 855 915 930   1020          1100  200
Paul: 1315 1355 1405

n: length of the badge records array
"""

"""
Algorithm:
    1. use map to store employee and their 1 hr access time in min_heap
    3. sort badge time by name and time
    2. iterate over the badge times
        - if current time is more than 1 hr from the top element,
            - pop top element and keep comparing
        - insert current time in min_heap
    3. return results where min_heap size is 3 or more times.
"""




from collections import defaultdict
import heapq
def find_employee(badge_times):
    result = {}
    if not badge_times:
        return result
    # employee name and min_heap
    employee_map = defaultdict(list)

    # sort badge_times
    badge_times.sort()

    for badge_time in badge_times:
        employee, time = badge_time
        # To return the first period where 3 or more times badges were scanned,
        # we are using this condition but it also limits the number of entries
        # in the first match to 3 which is not expected.
        # ???
        if len(employee_map[employee]) < 3:
            while employee_map[employee] and time - employee_map[employee][0] > 100:
                heapq.heappop(employee_map[employee])
            heapq.heappush(employee_map[employee], time)

    for employee, min_heap in employee_map.items():
        if len(min_heap) >= 3:
            result[employee] = min_heap

    return result


print(find_employee([
    ["Paul", 1355],
    ["Jennifer", 1910],
    ["John", 830],
    ["Paul", 1315],
    ["John", 1615],
    ["John", 1640],
    ["John", 835],
    ["Paul", 1405],
    ["John", 855],
    ["John", 930],
    ["John", 915],
    ["John", 730],
    ["Jennifer", 1335],
    ["Jennifer", 730],
    ["John", 1630],
]))
