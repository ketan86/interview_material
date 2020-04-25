# TrieNode => {children, is_end_word, char,
# mark_as_leaf(), unmark_as_leaf()}


def total_words(root):
    count = 0
    return _traverse(root, count)


def _traverse(node, count):
    for child in node.children:
        if child:
            if child.is_end_word:
                count += 1
            count = _traverse(child, count)
    return count
