#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (45.60%)
# Likes:    3528
# Dislikes: 388
# Total Accepted:    570.4K
# Total Submissions: 1.2M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a", "b", "c"]

# Note:
#
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
#
#

# @lc code=start
# pylint:skip-file


class Solution:
    def letterCombinations(self, digits):
        input_string = []

        if not digits:
            return input_string

        # create a map to store the digit and respective letters
        digit_map = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        # create a list of letters
        for digit in digits:
            input_string.append(digit_map[digit])

        # dfs to find all combinations
        return self.dfs(input_string, 0, len(input_string) - 1, memo={})

    def dfs(self, input_string, start, end, memo):
        # if start index > end index, we have reached the end of the list
        # return the list with empty string.
        if start > end:
            return ['']

        if input_string[start] in memo:
            memo[input_string[start]]

        result = []
        # iterate over the first letter and create new combinations
        # with remaining elements of the string
        # for ex,
        #                    ["abc", "def"]
        #              /                      \ same for "b" + ["def"]
        #           /                           and "c" + ["def"]
        #
        #         "a"   +    ["def"]  <- ["d", "e", "f"] = ["ad", "ae", "af"]
        #             / d    | e     \ f    <- return
        #      d + [''] e + [''] f + ['']
        #
        #
        #
        for char in input_string[start]:
            # find all the combination from start+1 to end and
            # create new combination with a char.
            for c in self.dfs(input_string, start + 1, end, memo):
                result.append(char + c)

        memo[input_string[start]] = result

        return result


print(Solution().letterCombinations('49'))

# @lc code=end
