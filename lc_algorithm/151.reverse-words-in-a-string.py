"""
151. Reverse Words in a String
Medium

1713

3298

Add to List

Share
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

Accepted
540,365
Submissions
2,182,416

"""


from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        """Runtime: 40 ms, faster than 31.07%"""
        # deque to append elements efficiently in left
        output = deque()
        left = 0
        right = len(s) - 1

        # remove leading and trailing spaces
        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        word = ''
        # iterate over the string
        while left <= right:
            # if char is empty, check if word was not empty
            if s[left] == ' ':
                # if word, append that to the output
                if word:
                    output.appendleft(word)
                    word = ''
            elif s[left] != ' ':
                word += s[left]
            left += 1

        # handle last word
        output.appendleft(word)

        return ' '.join(output)
