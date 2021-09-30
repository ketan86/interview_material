#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
"""
211. Design Add and Search Words Data Structure
Medium

3219

134

Add to List

Share
Design a data structure that supports adding new words and finding if a string
matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure
that matches word or false otherwise. word may contain dots '.' where dots
can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
Accepted
301,453
Submissions
725,980

"""

# @lc code=start

from collections import defaultdict


class WordDictionary:

    def __init__(self):
        """
        Runtime: 296 ms, faster than 79.26% 

        {
            'h' : {
                'e' : {
                    'l' : {
                        'l' : {
                            'o' : {
                                'end_word' : True
                            }
                        }
                    }
                },
                'i' : {
                    'end_word' : True
                }
            }

        }

        search "h." -> search "h" and then all it's child and if found, return
        True.

        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie

        for char in word:
            if not char in node:
                node[char] = {}
            node = node[char]
        node['end_word'] = True

    def search(self, word: str) -> bool:

        def search_in_node(word, node):
            # navigate through the tree one char at a time
            for index, char in enumerate(word):
                # if char not in node and not '.' return False
                if not char in node:
                    # if char is '.', we have to search all paths
                    if char == '.':
                        for x in node:
                            # except 'end_word' char, search all nodes for remaining char of the word
                            # if any direction we get the end word, return True
                            if x != 'end_word' and search_in_node(word[index+1:], node[x]):
                                return True
                    return False
                else:
                    node = node[char]
            # return True if we hit the end word
            return 'end_word' in node

        return search_in_node(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord('hello')
# param_2 = obj.search('.ello')
# @lc code=end
