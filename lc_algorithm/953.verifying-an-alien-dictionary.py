#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:

    def isAlienSorted(self, words, order: str) -> bool:
        # store char index using the order
        order_map = {}
        for index, value in enumerate(order):
            order_map[value] = index

        # go over the word index one at a time
        for word_index in range(len(words) - 1):
            current_word = words[word_index]
            next_word = words[word_index+1]

            # go over the current word characters
            for char_index in range(len(current_word)):

                # if current char index is greater than length of the next word
                if char_index >= len(next_word):
                    return False
                # if current char is not same, check if they are sorted and if not, return False
                if current_word[char_index] != next_word[char_index]:
                    # if current word char is > next word char
                    if order_map[current_word[char_index]] > order_map[next_word[char_index]]:
                        return False
                    break
        return True
# @lc code=end
