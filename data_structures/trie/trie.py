"""
Trie is an efficient information reTrieval data structure. Using Trie, search
complexities can be brought to optimal limit (key length). If we store keys in
binary search tree, a well balanced BST will need time proportional to M * log
N, where M is maximum string length and N is number of keys in tree. Using
Trie, we can search the key in O(M) time. However the penalty is on Trie
storage requirements (Please refer Applications of Trie for more details).

for ex, to store following words,
abc
abgl
cdf
abcd
lmn

1. root node does not contain value and not a word. It does contains
   childs.
                                root: ['a', None, ...], False, ''
                                 /
                 a: [None,'b', None, ...], False , 'a'
                        /
        b:[None, None, 'c', .. 'g', ..], False, 'b'
                /                               \
c:[], True, 'c'                                 g:[.. 'l', ''], False, 'g'
                                                        \
                                                         l:[], True, 'l'

"""


class TrieNode:
    def __init__(self, char=''):
        # assuming there are 26 upper or lower case alphabets.
        # use dict instead of list for storing wider char set.
        self.child = [None] * 26
        # indicates whether the word ends here or not.
        self.is_end_word = False
        # actual character stored at this location.
        self.char = char


class Trie:
    def __init__(self):
        # define a root node with no value.
        self.root = TrieNode()

    def get_index(self, t):
        # find the index value for each char in the child list.

        # In[26]: ord('a') - ord('a')
        # Out[26]: 0
        # In[27]: ord('b') - ord('a')
        # Out[27]: 1
        # In[29]: ord('c') - ord('a')
        # Out[29]: 2
        return ord(t) - ord('a')

    def insert(self, key):
        # lower the key
        key = key.lower()
        # copy root to current
        curr = self.root
        # using the key length, we can determine the level in which the char
        # of the key is stored,
        # for ex,
        #          a      <- 0 level (root)
        #        b        <- 1
        #      c
        #    d
        for level in range(len(key)):
            # find the index of the child list
            index = self.get_index(key[level])
            # if index value is not set on the child list, create a new
            # trie node at that index.
            if not curr.child[index]:
                curr.child[index] = TrieNode(key[level])
            # else, char of the key is already set and travel down the line.
            curr = curr.child[index]
        # mark the word complete.
        curr.is_end_word = True

    def search(self, key):
        # lower the key
        key = key.lower()
        curr = self.root
        # iterate of the key char
        for level in range(len(key)):
            # find the index of the char
            index = self.get_index(key[level])
            # if no trie node at that index, key is not present.
            if not curr.child[index]:
                return False
            # else, char is present and move to next char
            curr = curr.child[index]
        # if key is visited and word is complete, return true else false
        if curr.is_end_word:
            return True
        return False

    def delete(self, key):
        """
        Case 1: Word with No Suffix or Prefix
        -------------------------------------
        If the word to be deleted has no suffix or prefix and all the character
        nodes of this word do not have any other children, then we will delete
        all these nodes up to the root.

        However, if any of these nodes have other children (are part of another
        branch), then they will not be deleted. This will be explained further
        in Case 2.

        In the figure below, the deletion of the word bat would mean that we
        have to delete all characters of bat.

        Case 2: Word is a Prefix
        ------------------------
        If the word to be deleted is a prefix of
        some other word, then the value of is_end_word of the last node of that
        word is set to False and no node is deleted.

        For example, to delete the word the, we will simply unmark e to show
        that the word doesn’t exist anymore.


        Case 3: Word Has a Common Prefix
        --------------------------------
        If the word to be deleted has a common prefix and the last node of that
        word does not have any children, then this node is deleted along with
        all the parent nodes in the branch which do not have any other children
        and are not end characters.

        Take a look at the figure below. In order to delete their, we’ll
        traverse the common path up to the and delete the characters i and r.

        """

        # lower the key
        key = key.lower()
        # delete the key
        self._delete(key, 0, self.root)

    def _delete(self, key, level, node):
        deleted = False
        # if node is None, return
        if not node:
            return deleted
        # if last node is reached.
        if len(key) == level:
            # if no child for the node.
            if not any(node.child):
                # set node to None and set deleted
                node = None
                deleted = True
            # if there are child for the node.
            else:
                # unmark the node and set not deleted
                node.is_end_word = False
                deleted = False
        else:
            # get the index and retrive the child node
            index = self.get_index(key[level])
            child = node.child[index]
            # recursive call to find the next node
            child_deleted = self._delete(key, level + 1, child)
            # if child was deleted, mark current node
            if child_deleted:
                # set the node's child to None.
                node.child[index] = None
                # if node is ending with word, mark not deleted
                if node.is_end_word:
                    deleted = False
                # if there are child, cant mark deleted
                elif any(node.child):
                    deleted = False
                # if no child or not an end word, set node to none and set
                # deleted
                else:
                    node = None
                    deleted = True
            else:
                deleted = False

        return deleted


# t = Trie()
# # print(t.get_index('f'))
# t.insert("abcd")
# print(t.search("abc"))
# t.insert("ab")
# t.insert("abce")
# t.insert("abced")
# t.delete("abce")
# print(t.search("abce"))
# t.insert("abcdef")
# print(t.search("ab"))
# t.delete("ab")
# print(t.search("ab"))

# d = ['the', 'hello', 'there', 'answer', 'any',
#      'educative', 'world', 'their', 'abc']
# for i in d:
#     t.insert(i)


# def is_formation_possible(dictionary, word):
#     trie = Trie()
#     for w in dictionary:
#         trie.insert(w)

#     start_index = 0
#     end_index = 1
#     found = ''

#     while end_index <= len(word):
#         search_word = word[start_index:end_index]
#         if trie.search(search_word):
#             found += search_word
#             start_index = end_index
#         end_index += 1
#     return found == word


# print(is_formation_possible(d, 'helloworld'))
