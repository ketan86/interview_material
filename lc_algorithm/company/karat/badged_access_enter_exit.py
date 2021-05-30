"""
We are working on a security system for a badged-access room in our company's
building.

Given an ordered list of employees who used their badge to enter or exit the
room, write a function that returns two collections:

All employees who didn't use their badge while exiting the room - they recorded
an enter without a matching exit. (All employees are required to leave the room
before the log ends.)

All employees who didn't use their badge while entering the room - they recorded
an exit without a matching enter. (The room is empty when the log begins.)

Each collection should contain no duplicates, regardless of how many times a
given employee matches the criteria for belonging to it.

badge_records_1 = [
["Martha", "exit"],
["Paul", "enter"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "enter"],
["Paul", "enter"],
["Curtis", "exit"],
["Curtis", "enter"],
["Paul", "exit"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "exit"],
["Paul", "enter"],
["Paul", "enter"],
["Martha", "exit"],
]

Expected output: ["Curtis", "Paul"], ["Martha", "Curtis"]

Additional test cases:

badge_records_2 = [
["Paul", "enter"],
["Paul", "enter"],
["Paul", "exit"],
]

Expected output: ["Paul"], []

badge_records_3 = [
["Paul", "enter"],
["Paul", "exit"],
["Paul", "exit"],
]

Expected output: [], ["Paul"]

badge_records_4 = [
["Paul", "enter"],
["Paul", "exit"],
["Paul", "exit"],
["Paul", "enter"],
["Martha", "enter"],
["Martha", "exit"],
]

Expected output: ["Paul"], ["Paul"]

badge_records_5 = [
["Paul", "enter"],
["Paul", "exit"],
]

Expected output: [], []

badge_records_6 = [
["Paul", "enter"],
["Paul", "enter"],
["Paul", "exit"],
["Paul", "exit"],
]

Expected output: ["Paul"], ["Paul"]

badge_records_7 = [
["Paul", "enter"],
["Paul", "exit"],
["Paul", "exit"],
["Paul", "enter"],
]

Expected output: ["Paul"], ["Paul"]

n: length of the badge records array
"""


def find_employee(badge_records):
    """
    Steps:
        1. only record entries in the stack
        2. when re-entry is found, record that and delete old entry and add
           new entry in the stack.
        3. when exit is found, check if respective entry was recorded,
           - if entry was found, remove entry and do not record exit
           - if entry was not found, record the exit
    """
    invalid_entries = set()
    invalid_exits = set()
    stack = []
    temp_stack = []

    for employee, status in badge_records:
        # if status is exit
        if status == 'exit':
            # check the status for the entry
            while stack:
                e, s = stack.pop()
                # if same employee is found with entry, discard entry and exit
                # and continue.
                if e == employee:
                    break
                else:
                    temp_stack.append((e, s))
            else:
                # if employee entry is not found, record in invalid_exits set
                invalid_exits.add(employee)

            # move all temp stack entries back to stack
            while temp_stack:
                stack.append(temp_stack.pop())
        else:
            # if re-entry is found, remore prior entry and record re-entry
            while stack:
                e, s = stack.pop()
                if e == employee:
                    invalid_entries.add(e)
                    break
                else:
                    temp_stack.append((e, s))

            while temp_stack:
                stack.append(temp_stack.pop())

            # enter current entry
            stack.append((employee, status))

    # employee entered but never exited
    while stack:
        e, s = stack.pop()
        invalid_entries.add(e)

    return list(invalid_entries), list(invalid_exits)


badge_records_1 = [
    ["Martha", "exit"],
    ["Paul", "enter"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "enter"],
    ["Paul", "enter"],
    ["Curtis", "exit"],
    ["Curtis", "enter"],
    ["Paul", "exit"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "exit"],
    ["Paul", "enter"],
    ["Paul", "enter"],
    ["Martha", "exit"],
]
print(find_employee(badge_records_1))

badge_records_2 = [
    ["Paul", "enter"],
    ["Paul", "enter"],
    ["Paul", "exit"],
]
print(find_employee(badge_records_2))

badge_records_3 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
]
print(find_employee(badge_records_3))

badge_records_4 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
    ["Paul", "enter"],
    ["Martha", "enter"],
    ["Martha", "exit"],
]
print(find_employee(badge_records_4))

badge_records_5 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
]
print(find_employee(badge_records_5))

badge_records_6 = [
    ["Paul", "enter"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
]
print(find_employee(badge_records_6))

badge_records_7 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
    ["Paul", "enter"],
]
print(find_employee(badge_records_7))
