#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
""" 
432. All O`one Data Structure
Hard

831

104

Add to List

Share
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. 
    It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
 

Constraints:

1 <= key.length <= 10
key consists of lowercase English letters.
It is guaranteed that for each call to dec, key is existing in the data structure.
At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.

"""
# @lc code=start


class Node:
    """
    Stores count and all values belonging to that value.

    dummy_head(freq(0)) <-> 
        Node(freq(1) -> set("hoo", "jar")) <-> 
        Node(freq(2) -> set("foo", "bar")) <-> dummy_tail(freq(inf))

            foo      bar        far       foo
             x       |          /          |
             Node(1, 'bar', 'far')    -> Node(2, 'foo')    
    """

    def __init__(self, freq=0, prev=None, next=None):
        self.freq = freq
        self.keys = set()
        self.prev = prev
        self.next = next


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.

        1. Maintain dummy head with smallest value and dummy tail with 'inf' value
           - return one of the key from the head.next node as min.
           - return one of the key from the tail.prev node as max.

        2. Maintain two hash map.
           - one with key and it's freq

            # map key with freq
            # {
            #    'foo' : '2',
            #    'bar' : '2',
            #    'var' : '1'
            # }
           - another with freq and it's node

            # freq with pointer to a node that stores all keys
            # {         | <- tail
            #    '2' : Node(2, 'foo', 'bar'),
            #    '1' : Node(1, 'var')
            # }         | <- head

        Inc:
            1. find if key is present in freq_map.
                - if present in node_map, remove key from the node of the
                  node_map using the freq as key found.
                - increment the key freq in the freq_map and
                  check if next incremented freq is there in the node.next
                  found in node_map
                - if node.next freq is higher than expected, insert new node
                - if node.next freq is same, insert new key
            2. if key is not present in the freq_map
                - create a new node with freq as 1, insert current key in set
                - create a node_map with freq as 1 and node being the value
                - insert key in freq_map with current freq

        Dec:
            1. find if key is present in freq_map.
                - if present in node_map, remove key from the node of the
                  node_map using the freq as key found.
                - decrement the key freq in the freq_map and
                  check if next decremented freq is there in the node.prev
                  found in node.map
                - if node.freq freq is lesser than expected, insert new node
                - if node.next freq is same, insert new key

        getMax:
            1. find tail.prev node and return one of it's key

        getMin:
            2. find head.next node and return one of it's key

        """
        # smallest freq node stored after dummy head
        self.head = Node(0)

        # highest freq node stored before dummy head
        self.tail = Node(float('inf'), prev=self.head)
        self.head.next = self.tail

        # freq with pointer to a node that stores all keys
        # {         | <- tail
        #    '2' : Node(2, 'foo', 'bar'),
        #    '1' : Node(1, 'var')
        # }         | <- head
        self.node_map = {}

        # map key with freq
        # {
        #    'foo' : '2',
        #    'bar' : '2',
        #    'var' : '1'
        # }
        self.freq_map = {}

    def inc(self, key: str) -> None:
        """

        Inc:
            1. find if key is present in freq_map.
                - if present in node_map, remove key from the node of the
                  node_map using the freq as key found.
                - increment the key freq in the freq_map and
                  check if next incremented freq is there in the node.next
                  found in node_map
                - if node.next freq is higher than expected, insert new node
                - if node.next freq is same, insert new key
            2. if key is not present in the freq_map
                - create a new node with freq as 1, insert current key in set
                - create a node_map with freq as 1 and node being the value
                - insert key in freq_map with current freq
        """
        # if key is in the map, find it's freq and increment by 1 and create a
        # new node
        if key in self.freq_map:
            node = self.node_map[self.freq_map[key]]
            node.keys.remove(key)
            self.freq_map[key] += 1

            if node.next.freq > self.freq_map[key]:
                prev_node = node.prev
                next_node = node.next
                node = Node(self.freq_map[key], set(
                    [key]), prev_node, next_node)
                self.node_map[self.freq_map[key]] = node
            else:
                # same
                node = self.node_map[self.freq_map[key]]
                node.keys.add(key)

        else:
            node = Node(1, set([key]), self.head, self.tail)
            self.node_map[1] = node
            self.freq_map[key] = 1

    def dec(self, key: str) -> None:
        """
        Dec:
            1. find if key is present in freq_map.
                - if present in node_map, remove key from the node of the
                  node_map using the freq as key found.
                - decrement the key freq in the freq_map and
                  check if next decremented freq is there in the node.prev
                  found in node.map
                - if node.freq freq is lesser than expected, insert new node
                - if node.next freq is same, insert new key

        """
        if key in self.key_freq_map:
            node = self.node_map[self.freq_map[key]]
            node.keys.remove(key)
            self.freq_map[key] -= 1

            if node.prev.freq < self.freq_map[key]:
                prev_node = node.prev
                next_node = node.next
                node = Node(self.freq_map[key], set(
                    [key]), prev_node, next_node)
                self.node_map[self.freq_map[key]] = node
            else:
                # same
                node = self.node_map[self.freq_map[key]]
                node.keys.add(key)

    def getMaxKey(self) -> str:
        # if prev node of the tail is head, return ''
        if not self.tail.prev.val == 0:
            return ''
        else:
            return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        # if next node of the head is tail, return ''
        if not self.head.next.val == float('inf'):
            return ''
        return next(iter(self.head.next.keys))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end
