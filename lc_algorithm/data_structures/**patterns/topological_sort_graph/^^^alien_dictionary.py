"""
There is a dictionary containing words from an alien language for which
we don’t know the ordering of the characters. Write a method to find the
correct order of characters in the alien language.

Example 1:

Input: Words: ["ba", "bc", "ac", "cab"]
Output: bac
Explanation: Given that the words are sorted lexicographically by the rules
of the alien language, so
from the given words we can conclude the following ordering among its
characters:
 
1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
2. From "bc" and "ac", we can conclude that 'b' comes before 'a'
 
From the above two points, we can conclude that the correct character
order is: "bac"
Example 2:

Input: Words: ["cab", "aaa", "aab"]
Output: cab
Explanation: From the given words we can conclude the following ordering
among its characters:
 
1. From "cab" and "aaa", we can conclude that 'c' comes before 'a'.
2. From "aaa" and "aab", we can conclude that 'a' comes before 'b'
 
From the above two points, we can conclude that the correct character order
is: "cab"
Example 3:

Input: Words: ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
Output: ywxz
Explanation: From the given words we can conclude the following ordering among
its characters:
 
1. From "ywx" and "wz", we can conclude that 'y' comes before 'w'.
2. From "wz" and "xww", we can conclude that 'w' comes before 'x'.
3. From "xww" and "xz", we can conclude that 'w' comes before 'z'
4. From "xz" and "zyy", we can conclude that 'x' comes before 'z'
5. From "zyy" and "zwz", we can conclude that 'y' comes before 'w'
 
From the above five points, we can conclude that the correct character order
is: "ywxz"
"""

# pylint: skip-file
from collections import deque


def find_order(words):
    """
    By comparing adjacent word, we can determine the order of the char in
    the dictionary. we need to only compare the first different char between
    adjacent words to form the graph since words are in lexicographical
    order. By running the topological sort, we can determine the correct
    order of characters in the alien language.

    Input: Words: ["ba", "bc", "ac", "cab"]
    Output: bac

                        b
                        |
                        a
                        |
                        c


    """
    # initialize the graph
    in_degree = {char: 0 for word in words for char in word}
    graph = {char: [] for word in words for char in word}

    # build the graph
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for j in range(min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break

    print(graph, in_degree)
    # find all sources with in_degree 0
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # traverse the graph
    sorted_order = []
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # if sorted_order does not contain all the chars, there is a cycle.
    if len(sorted_order) != len(in_degree):
        return ""

    return "".join(sorted_order)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " +
          find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
