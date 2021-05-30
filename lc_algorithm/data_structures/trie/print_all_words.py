
# TrieNode => {children, is_end_word, char, mark_as_leaf(), unmark_as_leaf()}
from trie import Trie


def print_all_words(node, word):
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
            results += print_all_words(child, word + child.char)

    return results


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()
for key in keys:
    trie.insert(key)

print(print_all_words(trie.root, ''))
