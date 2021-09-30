"""
Given an array of words, find the longest string with words such that every
prefix of it is also in words

Example :

["a", "ap", "app"] -> "app"
["a", "bananna", "app", "appl", "ap", "apply", "apple"] -> "apple" instead of
"apply" because of the lexicographical order.

             a  b  
             p  a
             p  n 
             l  a
            e y n
                n
                a 


"""
from collections import defaultdict


class Node:
    def __init__(self, string=''):
        self.children = defaultdict(Node)
        self.string = string


class Solution:

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.string = word

    def find(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
            if not node.string:
                return

        if len(word) > len(self.ans):
            self.ans = word
        elif len(word) == len(self.ans) and word < self.ans:
            self.ans = word

    def longer_word(self, words):
        self.root = Node()
        self.ans = ''
        for word in words:
            self.insert(word)
        for word in words:
            self.find(word)
        return self.ans
