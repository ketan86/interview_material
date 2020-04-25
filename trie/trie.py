class TrieNode:
    def __init__(self, char=''):
        self.child = [None] * 26
        self.is_end_word = False
        self.char = char


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, t):
        return ord(t) - ord('a')

    def insert(self, key):
        key = key.lower()
        curr = self.root
        index = 0
        for level in range(len(key)):
            index = self.get_index(key[level])
            if not curr.child[index]:
                curr.child[index] = TrieNode(key[level])
            curr = curr.child[index]

        curr.is_end_word = True

    def search(self, key):
        key = key.lower()
        curr = self.root
        index = 0
        for level in range(len(key)):
            index = self.get_index(key[level])
            if not curr.child[index]:
                return False
            curr = curr.child[index]
        if curr.is_end_word:
            return True
        return False

    def delete(self, key):
        key = key.lower()
        self._delete(key, 0, self.root)

    def _delete(self, key, level, node):
        deleted = False
        if not node:
            return deleted

        if len(key) == level:
            if not any(node.child):
                node = None
                deleted = True
            else:
                node.is_end_word = False
                deleted = False
        else:
            # get the child node
            index = self.get_index(key[level])
            child = node.child[index]
            child_deleted = self._delete(key, level + 1, child)
            if child_deleted:
                node.child[index] = None
                if node.is_end_word:
                    deleted = False
                elif not any(node.child):
                    deleted = False
                else:
                    node = None
                    deleted = True
            else:
                deleted = False

        return deleted


t = Trie()
# print(t.get_index('f'))
# t.insert("abcd")
# t.insert("ab")
# t.insert("abce")
# t.insert("abcde")
# t.insert("abcdef")
# print(t.search("ab"))
# t.delete("ab")
# print(t.search("ab"))

d = ['the', 'hello', 'there', 'answer', 'any',
     'educative', 'world', 'their', 'abc']
for i in d:
    t.insert(i)


def is_formation_possible(dictionary, word):
    trie = Trie()
    for w in dictionary:
        trie.insert(w)

    start_index = 0
    end_index = 1
    found = ''
    import pdb
    pdb.set_trace()
    while end_index <= len(word):
        search_word = word[start_index:end_index]
        if trie.search(search_word):
            found += search_word
            start_index = end_index
        end_index += 1
    return found == word


print(is_formation_possible(d, 'helloworld'))
