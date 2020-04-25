# Create Trie => trie = Trie()
# TrieNode => {children, is_end_word, char,
# mark_as_leaf(), unmark_as_leaf()}
# get_root => trie.get_root()
# Insert a Word => trie.insert(key)
# Search a Word => trie.search(key) return true or false
# Delete a Word => trie.delete(key)


def find_words(root):
    result = []
    return traverse(root, result, '')


def traverse(root, result, word):
    for child in root.children:
        if child:
            word += child.char
            if child.is_end_word:
                result.append(word)
            result = traverse(child, result, word)
            word = word[:-1]
    return result
