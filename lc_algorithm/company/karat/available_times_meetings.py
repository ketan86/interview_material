"""
We are writing a tool to help users manage their calendars.
Given an unordered list of times of day when people are busy,
write a function that tells us the intervals during the day
when ALL of them are available.

Each time is expressed as an integer using 24-hour notation,
such as 1200 (12:00), 1530 (15:30), or 800 (8:00).

p1_meetings = [
  (1230, 1300),
  ( 845, 900),
  (1300, 1500),
]

p2_meetings = [
  ( 0, 844),
  ( 930, 1200),
  (1515, 1546),
  (1600, 2400),
]

p3_meetings = [
  ( 845, 915),
  (1515, 1545),
  (1235, 1245),
]

p4_meetings = [
  ( 1, 5),
  (844, 900),
  (1515, 1600)
]

schedules1 = [p1_meetings, p2_meetings, p3_meetings]
schedules2 = [p1_meetings, p3_meetings]
schedules3 = [p2_meetings, p4_meetings]

Expected output:

findAvailableTimes(schedules1)
 => [  844,  845 ],
    [  915,  930 ],
    [ 1200, 1230 ],
    [ 1500, 1515 ],
    [ 1546, 1600 ]

findAvailableTimes(schedules2)
 => [    0,  845 ],
    [  915, 1230 ],
    [ 1500, 1515 ],
    [ 1545, 2400 ]

findAvailableTimes(schedules3)
    [  900,  930 ],
    [ 1200, 1515 ]

n = number of meetings
s = number of schedules

"""


def find_available_times(schedule):
    # combined meeting list
    all_meetings = []

    # add all meetings into one meeting list
    for meetings in schedule:
        for meeting in meetings:
            all_meetings.append(meeting)

    # sort meeting by start and end time.
    all_meetings.sort()

    # merge meetings
    merged_meetings = []
    for meeting in all_meetings:
        if merged_meetings and meeting[0] < merged_meetings[-1][1]:
            merged_meetings[-1] = (
                min(merged_meetings[-1][0], meeting[0]),
                max(merged_meetings[-1][1], meeting[1])
            )
        else:
            merged_meetings.append(meeting)

    result = []
    # find available time
    for i in range(1, len(merged_meetings)):
        if merged_meetings[i][0] > merged_meetings[i-1][1]:
            result.append(
                [merged_meetings[i-1][1], merged_meetings[i][0]]
            )

    return result


p1_meetings = [
    (1230, 1300),
    (845, 900),
    (1300, 1500),


]

p2_meetings = [
    (0, 844),
    (930, 1200),
    (1515, 1546),
    (1600, 2400),
]

p3_meetings = [
    (845, 915),
    (1515, 1545),
    (1235, 1245),
]

p4_meetings = [
    (1, 5),
    (844, 900),
    (1515, 1600)
]

schedules1 = [p1_meetings, p2_meetings, p3_meetings]
schedules2 = [p1_meetings, p3_meetings]
schedules3 = [p2_meetings, p4_meetings]

print(find_available_times(schedules1))
print(find_available_times(schedules2))
print(find_available_times(schedules3))
