#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
"""
140. Word Break II
Hard

3418

447

Add to List

Share
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""


"""
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
        wordDict = set(wordDict)
        res = []

        def dfs(index, path):  # O(2^N)
            # when index is last index, add the path to the result with space
            # seperated.
            if index == len(s):
                res.append(" ".join(path))
            else:
                # go over all the words and check if current word starts with
                # one of the word in the dict, use that and search the reminaing
                # word in the dict.
                for word in wordDict:
                    if s[index:].startswith(word):  # O(W)
                        path.append(word)
                        dfs(index+len(word), path)
                        path.pop()

        dfs(0, [])
        return res


print(Solution().wordBreak("applepie", [
      "cat", "apple", "and", "pie", "dog", "app", "lep", "ie"]))
# @lc code=end
