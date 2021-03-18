
# TrieNode => {children, is_end_word, char, mark_as_leaf(), unmark_as_leaf()}
from trie import Trie


def total_words(node):
    # store count
    count = 0

    # if node contains the word ending, increment the result
    if node.is_end_word:
        count += 1

    # traverse through all child
    for child in node.child:
        # if child is not none, find words in all other child.
        if child:
            # Recursively return the word count
            count += total_words(child)
    return count


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()
for key in keys:
    trie.insert(key)

print(total_words(trie.root))
