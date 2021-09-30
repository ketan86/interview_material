"""
Given an input string  and dictionary of words, segment the input string into a
space separeted sequence of dictionary words if possible.

Example:
Input: "applepie" , ["apple", "pie"] -> "apple pie"



Questions:
1. If word is present entirely and in segments, what do you return.
2. Multiple answers, return any
3. When not present, return None

"""
# @lc code=start
"""
catsanddog
 c & atsanddog
       ca & tsanddog
             cat & sanddog
                    cats & anddog
                            .....
 sanddog
  s & anddog
    sa & nddog
        ..
            sand & dog
    
 dog 
    return 

 " dog"
"""


class Solution:
    def wordBreak(self, s: str, wordDict):
        word_dict_set = set(wordDict)
        return self.dfs(s, word_dict_set)

    def dfs(self, s, word_dict_set):
        # if entire string is present
        if s in word_dict_set:
            return s

        # separate word in parts and checks if remaining is present
        # "applepie"
        # "a" present  & "applepie" present ?
        # "ap" present & "plepie" present
        for i in range(1, len(s)):
            if s[:i] in word_dict_set:
                result = self.dfs(s[i:], word_dict_set)
                if result is not None:
                    return s[:i] + " " + result


print(Solution().wordBreak("applepiecat", [
      "cat", "apple", "and", "pie", "dog"]))
# @lc code=end
