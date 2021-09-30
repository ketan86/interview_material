"""
340. Longest Substring with At Most K Distinct Characters
Medium

1695

60

Add to List

Share
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 

Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50
Accepted
204,928
Submissions
445,370

"""
# @lc code=start

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Runtime: 88 ms, faster than 47.44%"""
        freq_map = defaultdict(int)

        longest = 0
        start = 0
        end = 0

        # slide window one char at a time
        while end < len(s):
            # update the freq
            freq_map[s[end]] += 1

            # shrink window until k elements are left in the window
            while len(freq_map) > k:
                freq_map[s[start]] -= 1
                if freq_map[s[start]] == 0:
                    freq_map.pop(s[start])
                start += 1

            # find max distinct chars when len(freq_map) == k
            longest = max(longest, end - start + 1)

            end += 1

        return longest


print(Solution().lengthOfLongestSubstringKDistinct(s="eceba", k=2))
print(Solution().lengthOfLongestSubstringKDistinct(s="aa", k=1))
# @lc code=end
