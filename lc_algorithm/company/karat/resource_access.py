"""
Suppose we have an unsorted log file of accesses to web resources. Each log
entry consists of an access time, the ID of the user making the access, and the
resource ID.

The access time is represented as seconds since 00:00:00, and all times are
assumed to be in the same day.

For example:

logs = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_4", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_2"],
["54359", "user_1", "resource_3"],
]

Question:
Write a function that takes the logs and returns each users min and max access timestamp

Output:
user_3: [53760, 53760]
user_2: [54060, 62314]
user_1: [54001, 58523]
user_7: [400, 400]
user_6: [2, 215]
user_5: [53651, 53651]
user_4: [58522, 58522]
user_8: [100, 100]

Follow-up:

Write a function that takes the logs and returns the resource with the highest
number of accesses in any 5 minute window, together with how many accesses it
saw.

Example: ('resource_3', 3)

"""
from collections import defaultdict
import heapq


def min_max_access(logs):
    result = {}

    for time, user_id, _ in logs:
        time = int(time)
        # if user id not in result, set current time as min/max
        if user_id not in result:
            result[user_id] = [time, time]
        else:
            # if current time < min, set current to min
            if time < result[user_id][0]:
                result[user_id][0] = time
            # if current time > max, set current to max
            if time > result[user_id][1]:
                result[user_id][1] = time

    return result


def max_resource_access(logs):
    # min heap to maintain the resource with access of 5 min
    resource_map = defaultdict(list)
    max_resource_access = 0
    max_resource_name = ''
    # sort logs by resource id, timestamp
    logs.sort(key=lambda x: (x[2], x[0]))

    for time, user_id, resource in logs:
        time = int(time)

        # until min heap is not empty and time not within 5 min window.
        while resource_map[resource] and time - resource_map[resource][0] > 300:
            heapq.heappop(resource_map[resource])

        # add current entry
        heapq.heappush(resource_map[resource], time)

        # calculate max resource by checking the length of the heap
        max_resource_access_new = max(
            max_resource_access, len(resource_map[resource]))
        if max_resource_access_new != max_resource_access:
            max_resource_name = resource
            max_resource_access = max_resource_access_new

    return max_resource_name, max_resource_access


logs = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_4", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_2"],
    ["54359", "user_1", "resource_3"],
]

print(min_max_access(logs))
print(max_resource_access(logs))


logs = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_2"],
    ["58522", "user_4", "resource_1"],
    ["53651", "user_5", "resource_1"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_2"],
    ["54002", "user_1", "resource_3"],
]
print(max_resource_access(logs))
