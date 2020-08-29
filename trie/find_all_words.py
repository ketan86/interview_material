
# TrieNode => {children, is_end_word, char, mark_as_leaf(), unmark_as_leaf()}
from trie import Trie


def find_words(node, word):
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
            result += find_words(child, word + child.char)

    return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()
for key in keys:
    trie.insert(key)

print(find_words(trie.root, ''))
