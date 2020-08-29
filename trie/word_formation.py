
# TrieNode => {children, is_end_word, char, mark_as_leaf(), unmark_as_leaf()}
from trie import Trie


def is_formation_possible(keys, word):

    # create trie
    trie = Trie()
    # insert keys into the trie
    for key in keys:
        trie.insert(key)

    node = trie.root

    for i in range(len(word)):
        # get index of the current char
        index = trie.get_index(word[i])

        # check if child node is not None.
        if node.child[index] is None:
            return False

        # if child node contains the end, send the rest of the string
        # for search. if rest of the string is also found in trie, return
        # true.
        if node.child[index].is_end_word:
            if trie.search(word[i + 1:]):
                return True
        else:
            node = node.child[index]

    return False


keys = ["the", "hello", "there", "answer",
        "any", "educative", "world", "their", "abc"]
print(is_formation_possible(keys, "helloworl"))
