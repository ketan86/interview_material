# 362. Design Hit Counter Medium

# Share Design a hit counter which counts the number of hits received in the
# past 5 minutes (i.e., the past 300 seconds).

# Your system should accept a timestamp parameter (in seconds granularity), and
# you may assume that calls are being made to the system in chronological order
# (i.e., timestamp is monotonically increasing). Several hits may arrive roughly
# at the same time.

# Implement the HitCounter class:

# HitCounter() Initializes the object of the hit counter system. void hit(int
# timestamp) Records a hit that happened at timestamp (in seconds). Several hits
# may happen at the same timestamp. int getHits(int timestamp) Returns the
# number of hits in the past 5 minutes from timestamp (i.e., the past 300
# seconds).
 

# Example 1:

# Input
# ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
# [[], [1], [2], [3], [4], [300], [300], [301]]
# Output
# [null, null, null, null, 3, null, 4, 3]

# Explanation
# HitCounter hitCounter = new HitCounter();
# hitCounter.hit(1);       // hit at timestamp 1.
# hitCounter.hit(2);       // hit at timestamp 2.
# hitCounter.hit(3);       // hit at timestamp 3.
# hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
# hitCounter.hit(300);     // hit at timestamp 300.
# hitCounter.getHits(300); // get hits at timestamp 300, return 4.
# hitCounter.getHits(301); // get hits at timestamp 301, return 3.

# Constraints:

# 1 <= timestamp <= 2 * 109 All the calls are being made to the system in
# chronological order (i.e., timestamp is monotonically increasing). At most 300
# calls will be made to hit and getHits.
 

# Follow up: What if the number of hits per second could be huge? Does your
# design scale?

"""
https://leetcode.com/discuss/interview-question/178662/Design-a-Hit-Counter

How to handle concurrent requests?

When two requests update the list simultaneously, there can be race conditions.
It’s possible that the request that updated the list first may not be included
eventually.

The most common solution is to use a lock to protect the list. Whenever someone
wants to update the list (by either adding new elements or removing the tail), a
lock will be placed on the container. After the operation finishes, the list
will be unlocked.

This works pretty well when you don’t have a large volume of requests or
performance is not a concern. Placing a lock can be costly at some times and
when there are too many concurrent requests, the lock may potentially block the
system and becomes the performance bottleneck.

Distribute the counter

When a single machine gets too many traffic and performance becomes an issue,
it’s the perfect time to think of distributed solution. Distributed system
significantly reduces the burden of a single machine by scaling the system to
multiple nodes, but at the same time adding complexity.

Let’s say we distribute visit requests to multiple machines equally. I’d like to
emphasize the importance of equal distribution first. If particular machines get
much more traffic than the rest machines, the system doesn’t get to its full
usage and it’s very important to take this into consideration when designing the
system. In our case, we can get a hash of users email and distribute by the hash
(it’s not a good idea to use email directly as some letter may appear much more
frequent than the others).

To count the number, each machine works independently to count its own users
from the past minute. When we request the global number, we just need to add all
counters together.

Reference: https://aonecode.com/getArticle/211
http://blog.gainlo.co/index.php/2016/09/12/dropbox-interview-design-hit-counter/

You can connect with me here: https://www.linkedin.com/in/shashi-bhushan-kumar-709a05b5/


"""
import heapq

class HitCounterHeapNotOptimal:
    """
    Runtime: 28 ms, faster than 81.94%
    
    TimeComplexity:
        1. hit -> 0(n * log n) (delete) + 0(log n) (insert) => 0(n *log n)
        2. getHits -> 0(n * log n) (delete) + 0(1) (counting length) => 0(n *log n)

    SpaceComplexity => 0(n) -> where n = hits/second * 5 min

    NOTE: This solution creates 1 entry per hit even if the hit was at the same
    time. Even by using data structure like tuple(timestamp, no_of_hits), the
    update to last timestamp that is at the bottom of the min_heap would be
    difficult.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_heap = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.deleteOutdatedHits(timestamp)
        heapq.heappush(self.min_heap, timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.deleteOutdatedHits(timestamp)
        return len(self.min_heap)

    def deleteOutdatedHits(self, timestamp: int) -> None:
        """Delete hits that are not within 5 min window size.

        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.min_heap and timestamp - self.min_heap[0] >= 300:
            heapq.heappop(self.min_heap)

from collections import deque

class HitCounterDequeue:
    """
    Runtime: 32 ms, faster than 58.04%

    TimeComplexity:
        1. hit -> 0(1) (delete) + 0(1) (insert) => 0(1)
        2. getHits -> 0(1) (delete) + 0(1) (counting length) => 0(1)

    SpaceComplexity => 0(300) -> where n = hits/second * 5 min

    This soultion works because the order in which hits are based on the
    monotonically incresing timestamp so no ordering is required.
    """
    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()

        return len(self.queue)


class HitCounterDequeueOptimized:
    """
    Runtime: 32 ms, faster than 57.62%

    TimeComplexity:
        1. hit -> 0(1) (delete) + 0(1) (insert) => 0(1)
        2. getHits -> 0(1) (delete) + 0(1) (counting length) => 0(1)

    SpaceComplexity => 0(n) -> where n = hits/second * 5 min
        ***** optimized space by combining all hits of the given timestamp.

    Queue solution can be optimized by storing queue<timestamp, no_of_hits>
    for better space complexity.
    """
    def __init__(self):
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        while self.queue and timestamp - self.queue[0][0] >= 300:
            self.queue.popleft()

        # if last timestamp is same, increment the count or append
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1] = (timestamp, self.queue[-1][1] + 1)
        else:
            self.queue.append((timestamp, 1))

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0][0] >= 300:
            self.queue.popleft()

        # count hits by adding all hits of each timestamp
        hits = 0
        for queue_item in self.queue:
            hits += queue_item[1]
        return hits

class HitCounterCircularArrayOptimized:
    """
    Runtime: 36 ms, faster than 17.18%

    This soultion maintains two arrays of size window.

    1. timestamps -> at each index, we store the timestamp
        0 1 2 3 4 5  <- index
       [0 0 0 0 0 0] <- timestamps
       [1 0 0 0 0 0]
       [1 2 0 0 0 0]
       [1 2 3 0 0 0]
       [1 2 3 4 0 0]
       ....
       [7 2 3 4 5 6]
       [7 8 3 4 5 6]

    2. hits       -> at each index, we store the hits, after it circulates
                     hits are reset to 1
        0 1 2 3 4 5  <- index
       [0 0 0 0 0 0] <- hits
       [1 0 0 0 0 0]
       [1 1 0 0 0 0]
       [1 1 1 0 0 0]
       [1 1 2 0 0 0] <- same timestamp
       [1 1 2 1 0 0]
       ....
       [1 1 2 1 1 1]
       [1 1 2 1 1 1]

    """
    def __init__(self, window=300):
        """
        Initialize your data structure here.
        """
        self.timestamps = [0] * window
        self.hits = [0] * window
        self.window = window

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # find the index in circular array
        index = timestamp % self.window

        # if timestamp is not found in timestamp array, timestamp has
        # circulated so reset the timestamp and set hits to 1
        if self.timestamps[index] != timestamp:
            self.timestamps[index] = timestamp
            self.hits[index] = 1
        # else, increment the hit count
        else:
            self.hits[index] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        hits = 0
        # count all hits where difference between given timestamp and current
        # timestamp is less than window size.
        for i in range(self.window):
            # [4,5,6,1,2,3] -> timestamp = 8, window 6
            if timestamp - self.timestamps[i] < self.window:
                hits += self.hits[i]
        return hits

# Your HitCounter object will be instantiated and called as such:
obj = HitCounterDequeue()
obj.hit(1)
obj.hit(1)
obj.hit(2)
obj.hit(3)
print(obj.getHits(4))
obj.hit(300)
print(obj.getHits(300))
print(obj.getHits(301))
