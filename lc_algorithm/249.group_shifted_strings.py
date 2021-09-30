"""
249. Group Shifted Strings
Medium

820

164

Add to List

Share
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence:
    "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the
    same shifting sequence. You may return the answer in any order.


Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]

Constraints:

1 <= strings.length <= 200
1 <= strings[i].length <= 50
strings[i] consists of lowercase English letters.
"""
from collections import defaultdict


class Solution:
    def groupStrings(self, strings):
        """
        Time: O(n log n) where n is length of all chars
        Space: O(n)
        """
        groups = defaultdict(list)

        for string in strings:
            mark = tuple([(ord(c)-ord(string[0])) % 26 for c in string])
            groups[mark].append(string)

        return groups.values()


print(Solution().groupStrings(
    ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
