#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# Hard

# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words, the
# empty slots on the left will be assigned more spaces than the slots on the
# right.

# For the last line of text, it should be left justified and no extra space
# is inserted between words.

# note:
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.


# Example 1:

# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."],
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation:
#   Note that the last line is "shall be    " instead of "shall     be",
#   because the last line must be left-justified instead of fully-justified.

# Note that the second line is also left-justified because it contains only one word.

# Example 3:

# Input:
# words = ["Science","is","what","we","understand","well","enough","to",
#         "explain","to","a","computer.","Art","is","everything","else",
#         "we","do"],
# maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]


# Constraints:

# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth

# @lc code=start
class Solution:
    def fullJustify(self, words, max_width):
        """
        Runtime: 28 ms, faster than 82.32% of Python3

        Strategy:
        1. find out which words should be in which line using greedy approach
        2. If a line is the last line or there is only one word, perform left
           justification
        3. Else, for line where more than one words exist, perform center
           justification.
        """
        result = []

        i = 0
        # move i until end word
        while i < len(words):
            word_len = len(words[i])

            # j pointer to move from i + 1 till the word length goes beyond max
            # width
            j = i + 1

            while j < len(words) and word_len <= max_width:
                # consider 1 min space between words
                word_len += 1 + len(words[j])
                j += 1

            # move one step back if word length exceeded max width
            if word_len > max_width:
                j -= 1

            # create string that is either left or center justified.
            # NOTE: move j one step back
            result.append(
                self.helper(words, i, j - 1, max_width, j == len(words)))

            i = j

        return result

    def helper(self, words, i, j, max_width, is_last_line):

        # output string
        string = ''

        # if both words are same or last line, left justify
        if j - i == 0 or is_last_line:
            # append equal amount of spaces between words
            string = ' '.join(words[i:j+1])
            # additional spaces to the end of the string.
            string += ' ' * (max_width - len(string))
        else:
            # center justification logic

            # Steps:
            # 1. find total characters by counting words
            # 2. find total spaces that we can put between each word
            # 3. divide total spaces by word count to find the even number
            #    of spaces we can for sure have between words
            # 4. module total spaces by word to find the extra spaces we
            #    can put starting from left to right
            #    - we are gurantied to have extra spaces 1 or more less than
            #      base spaces.
            # 5. put base spaces and 1 extra space from the extra spaces to
            #    create expected spaces.
            total_chars = sum([len(words[i]) for i in range(i, j+1)])
            total_spaces = max_width - total_chars
            base_spaces = total_spaces // (j - i)
            extra_spaces = total_spaces % (j - i)

            # append first word
            string = words[i]
            # from second till end word
            for k in range(i+1, j+1):
                # add base spaces and one extra space if we have extra spaces
                string += ' ' * (base_spaces + (1 if extra_spaces > 0 else 0))
                # add new word
                string += words[k]
                # reduce extra space
                extra_spaces -= 1
        return string


print(Solution().fullJustify(
    ["This", "is", "an", "example", "of", "text", "justification."], 16))

# @lc code=end
