#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

"""
380. Insert Delete GetRandom O(1) Medium

3737

217

Add to List

Share Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object. bool insert(int val)
Inserts an item val into the set if not present. Returns true if the item was
not present, false otherwise. bool remove(int val) Removes an item val from the
set if present. Returns true if the item was present, false otherwise. int
getRandom() Returns a random element from the current set of elements (it's
guaranteed that at least one element exists when this method is called). Each
element must have the same probability of being returned. You must implement the
functions of the class such that each function works in average O(1) time
complexity.

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert",
    "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains[1, 2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains[2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""

# @lc code=start
import random


class RandomizedSet:
    """Runtime: 96 ms, faster than 73.88 % 

    Time complexity: 
        GetRandom is always O(1). 
        Insert and Delete both have O(1) average time complexity, and 
            O(N) in the worst-case scenario when the operation exceeds
            the capacity of currently allocated array/hashmap and invokes
            space reallocation.

    Space complexity: O(N), to store N elements.

    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # stores value <-> index of the list where element is stored
        self.dict = {}
        # stores values at index
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.

        1. Insert value to map and assign last index of as it's value
        2. Insert new value to list.
        """
        if val in self.dict:
            return False

        # set last index of the list to dict value
        self.dict[val] = len(self.list)
        # append value to list
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.

        1. Find the index of the value from the map
        2. Swap value at that index in list with last index and then remove the
           last index.
        3. Update the index of the swapped element in the map.
        4. Remove the value from the map.
        """
        if val not in self.dict:
            return False

        # find the index where element need to be removed
        index = self.dict[val]

        # instead of removing the element from it's original position,
        # swap element with last element and pop last element.
        # NOTE: This is needed to avoid shifting all elements from the list as
        # well as updates required in map that maps elements to some index.
        # This works when order of the elements in the list has not to be
        # maintained.
        last_index = len(self.list) - 1

        # move last element to current element
        self.list[index] = self.list[last_index]
        # update last element index in dict
        self.dict[self.list[last_index]] = index

        # pop last element
        self.list.pop()

        self.dict.pop(val)

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
