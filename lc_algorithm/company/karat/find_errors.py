"""
Given a collection of actions and userIds, an error occurs when a userId takes
a specific action in order for example,

A => B => C : This sequence of actions yields error

Write a function that takes in a list of (Actions, UserIds) pairs and returns 
the user Id that encounters the error.

Sample Input:

action_user_1 = [
["A", "1"], <- A(1)
["B", "1"], <- B(1)
["B", "2"],
["C", "1"], <- C(1)
["C", "2"],
["C", "3"],
["A", "2"],  <- A(2)
["A", "3"], 
["A", "2"],
["B", "2"],  <- B(2)
["C", "2"], <- C(2)
]

Error action -> ["ABC"]
Expected output -> [1,2]

action_user_2 = [
["A", "1"],
["A", "1"]
["A", "1"]
["B", "1"],
["B", "2"], <- B
["C", "2"],
["C", "2"],
["C", "3"],
["A", "2], <- A
["A", "3"],
["A", "2"],
["B", "2],
["C", "2"], <- C
]

Error action -> ["BAC"]
Expected output -> [2]
"""
from collections import defaultdict


def find_userids(actions, error_string):
    result = []
    user_id_actions = defaultdict(list)

    for action, userid in actions:
        user_id_actions[userid].append(action)

    for userid, actions in user_id_actions.items():
        # even if substring of the actions (ABCDE actions) == error_string
        # we found the userid.
        count = ''.join(actions).count(error_string)
        if count:
            result.append(userid)

    return result


action_user_1 = [
    ["A", "1"],
    ["B", "1"],
    ["B", "2"],
    ["C", "1"],
    ["C", "2"],
    ["C", "3"],
    ["A", "2"],
    ["A", "3"],
    ["A", "2"],
    ["B", "2"],
    ["C", "2"],
]

print(find_userids(action_user_1, "ABC"))
print(find_userids(action_user_1, "CA"))
