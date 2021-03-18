"""
Given a string, sort it based on the decreasing frequency of its characters.

Example 1:

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear
before any other character.
Example 2:

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c'
appeared only once.
"""

# pylint: skip-file
import heapq
from collections import defaultdict


def sort_character_by_frequency(s):
    freq_map = defaultdict(int)
    for char in s:
        freq_map[char] += 1

    # create a max heap and store freq and char (heap sorted by freq)
    char_heap = []
    for char, freq in freq_map.items():
        heapq.heappush(char_heap, (-freq, char))

    # pop element and form a new string
    output_str = ''
    while char_heap:
        freq, char = heapq.heappop(char_heap)
        output_str += char * -freq

    return output_str


def main():

    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
