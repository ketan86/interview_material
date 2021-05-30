"""
Problem Statement #
Given an array of lowercase letters sorted in ascending order, find the smallest
letter in the given array greater than a given ‘key’.

Assume the given array is a circular list, which means that the last letter is
assumed to be connected with the first letter. This also means that the smallest
letter in the given array is greater than the last letter of the array and is
also the first letter of the array.

Write a function to return the next letter of the given ‘key’.

Example 1:

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.
Example 2:

Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.
Example 3:

Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest
letter greater than 'm' is 'a'.
Example 4:

Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest
letter greater than 'h' is 'a'.
"""
# pylint: skip-file


def search_next_letter_another_version(letters, key):
    start = 0
    end = len(letters) - 1
    if key < letters[start] or key > letters[end]:
        return letters[start]

    while start <= end:
        mid = start + (end - start) // 2
        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1

    if start > end:
        return letters[start]
    return letters[0]


def search_next_letter(letters, key):
    start_index = 0
    end_index = len(letters) - 1

    # if key is greather or equal to last index or less or euqal to 0,
    # return first index
    if key >= letters[end_index] or key <= letters[start_index]:
        return letters[start_index]

    # iterate over the array
    while start_index <= end_index:
        mid = start_index + (end_index - start_index) // 2
        if key < letters[mid]:
            end_index = mid - 1
        elif key > letters[mid]:
            start_index = mid + 1
        else:
            return letters[mid+1]

    # return end_index+1
    return letters[end_index + 1]


def main():
    print(search_next_letter(['b', 'c', 'f', 'h'], 'a'))
    print(search_next_letter_another_version(['b', 'c', 'f', 'h'], 'a'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter_another_version(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter_another_version(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h', 'j'], 'b'))
    print(search_next_letter_another_version(['a', 'c', 'f', 'h', 'j'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h', 'k'], 'g'))
    print(search_next_letter_another_version(['a', 'c', 'f', 'h', 'k'], 'g'))
    print(search_next_letter(['a', 'c', 'f', 'h', 'l'], 'j'))
    print(search_next_letter_another_version(['a', 'c', 'f', 'h', 'l'], 'j'))
    print(search_next_letter(['a', 'c', 'f', 'h', 'l'], 'd'))
    print(search_next_letter_another_version(['a', 'c', 'f', 'h', 'l'], 'd'))
    print(search_next_letter(['a', 'c', 'f', 'h', 'l', 'z'], 'y'))
    print(search_next_letter_another_version(
        ['a', 'c', 'f', 'h', 'l', 'z'], 'y'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter_another_version(['a', 'c', 'f', 'h'], 'm'))


main()
