#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (45.13%)
# Likes:    3638
# Dislikes: 56
# Total Accepted:    347.2K
# Total Submissions: 694.8K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
'[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
#
#
# Note:
#
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
#
#
#

# @lc code=start


class TrieNode:
    def __init__(self, char, end_word=False):
        self.char = char
        self.end_word = end_word
        self.child = [None] * 26


class Trie:

    def __init__(self):
        """
        Runtime: 264 ms, faster than 15.42%

        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def get_index(self, char):
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # levels we have to iterate over the trie is equal to the length
        # of the word.
        levels = len(word)
        # save the root.
        curr = self.root
        for i in range(levels):
            index = self.get_index(word[i])
            # if char is not set at the index of the child list, we need
            # to create a new TrieNode. else, it already exist so continue.
            if not curr.child[index]:
                curr.child[index] = TrieNode(word[i])
            curr = curr.child[index]
        curr.end_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        levels = len(word)
        curr = self.root
        for i in range(levels):
            index = self.get_index(word[i])
            # if char is not found at the index of the child list, word
            # does not exist.
            if not curr.child[index]:
                return False

            curr = curr.child[index]
        # if we found all the chars of the word in the trie but if end char
        # is not marked end_word, word does not exist.
        if not curr.end_word:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the
        given prefix.
        """
        level = len(prefix)
        curr = self.root
        for i in range(level):
            index = self.get_index(prefix[i])
            # if char is not found at the index of the child list, word
            # does not exist.
            if not curr.child[index]:
                return False
            curr = curr.child[index]

        # NOTE: prefix does not have to a complete word, so we don't check
        # if last char of the prefix word is a end word or not.
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
