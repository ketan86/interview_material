"""
https://leetcode.com/discuss/interview-question/925401/Robolox-Karat-or-SDE-or-San-Mateo

You are running a classroom and suspect that some of your students are passing
around the answers to multiple choice questions disguised as random strings.

Your task is to write a function that, given a list of words and a string, finds
and returns the word in the list that is scrambled up inside the string, if any
exists. There will be at most one matching word. The letters don't need to be
contiguous.


Example:
words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
string1 = 'tcabnihjs'
find_embedded_word(words, string1) -> cat

string2 = 'tbcanihjs'
find_embedded_word(words, string2) -> cat

string3 = 'baykkjl'
find_embedded_word(words, string3) -> None

string4 = 'bbabylkkj'
find_embedded_word(words, string4) -> baby

string5 = 'ccc'
find_embedded_word(words, string5) -> None

string6 = 'nbird'
find_embedded_word(words, string6) -> bird

n = number of words in words
m = maximal string length of each word
"""
from collections import Counter


def find_embedded_word(words, string):
    """
    from collections import Counter
    x = Counter("cats")
    y = Counter("tacs")
    z = Counter("kats")

    print(x - y)  # prints Counter()
    print(x - z)  # prints Counter({'c': 1})
    """
    # count the freq of each char of string
    string_count = Counter(string)
    # counts -> Counter(
    # {'t': 1, 'c': 1, 'a': 1, 'b': 1, 'n': 1, 'i': 1, 'h': 1, 'j': 1, 's': 1})

    # iterate over the words
    for word in words:
        # count the freq of each char in word
        word_count = Counter(word)
        # word_count -> Counter({'c': 1, 'a': 1, 't': 1})

        # after subtracting all word_count freq from string_count, if we get
        # empty counter, we found the word.
        if not (word_count - string_count):
            # (Pdb) word_count - counts
            # Counter()
            return word
    return None


words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
string = 'tcabnihjs'

print(find_embedded_word(words, string))
