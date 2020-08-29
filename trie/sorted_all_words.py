
# TrieNode => {children, is_end_word, char, mark_as_leaf(), unmark_as_leaf()}
from trie import Trie

# NOTE: words searched in trie would always be sorted due to pre-order
# traversal and sorted letters in alphabetical order.


def sort_list(node, word):
    # define result
    result = []

    # if node contains the word ending, increment the result
    if node.is_end_word:
        result.append(word)

    # traverse through all child
    for child in node.child:
        # if child is not none, find words in all other child.
        if child:
            # Recursively return the word count
            result += sort_list(child, word + child.char)

    return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()
for key in keys:
    trie.insert(key)

print(sort_list(trie.root, ''))
