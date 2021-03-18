
# TrieNode => {children, is_end_word, char, mark_as_leaf(), unmark_as_leaf()}
from trie import Trie

# NOTE: words searched in trie would always be sorted due to pre-order
# traversal and sorted letters in alphabetical order.


def sort_all_words(node, word):
    # store the results
    results = []

    # if node contains the end char, append the word
    if node.is_end_word:
        results.append(word)

    # traverse through all child of the current node
    for child in node.child:
        # if child is not none, find words in all other child.
        if child:
            # Recursively return the words
            results += sort_all_words(child, word + child.char)

    return results


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()
for key in keys:
    trie.insert(key)

print(sort_all_words(trie.root, ''))
