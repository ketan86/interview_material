#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#
"""
1189. Maximum Number of Balloons
Easy

607

50

Add to List

Share
Given a string text, you want to use the characters of text to form as many 
instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of 
instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
Accepted
67.8K
Submissions
109.4K
"""

# @lc code=start
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # count the freq of balloon word
        word = Counter('balloon')

        # count the freq of the ballon word in the given text
        word_freq = Counter()
        for char in text:
            if char in word:
                word_freq[char] += 1

        # divide each char freq and the min would be max balloon word we can
        # find
        # e.g.
        # c1 = Counter({'l': 2, 'o': 2, 'b': 1, 'a': 1, 'n': 1}) -> 'balloon'
        # c2 = Counter({'l': 4, 'o': 4, 'n': 2, 'b': 2, 'a': 2}) -> 'loonbalxballpoon'
        # max balloon will be min(freq_c2/freq_c1) of all char
        return min(word_freq[char] // word[char] for char in word)


print(Solution().maxNumberOfBalloons('loonbalxballpoon'))

# @lc code=end
