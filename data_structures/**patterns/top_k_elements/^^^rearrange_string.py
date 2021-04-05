"""
Given a string, find if its letters can be rearranged in such a way that no
two same characters come next to each other.

Example 1:

Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each
other.
Example 2:

Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.
Example 3:

Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come
together e.g., "apaa", "paaa".
"""
# pylint: skip-file
import heapq
from collections import defaultdict

# O(N *log N)


def rearrange_string(s):
    """
    Runtime: 36 ms, faster than 38.03%

    Use freq map to store the freq of each char. Consume max item first
    until all items are consumed or result's last char does not match with
        char of max heap top item.

    "vvvlo" -> {v->3, l->1, o->1} - result = ''
    1. consume v  -> {v->2, l->1, o->1} - result = "v"
    2. consume l (cause v can't be consumed again) -> {v->2, l->0, o->1} - result = "vl"
    3. consume v  -> {v->1, l->0, o->1} - result = "vlv"
    4. consume o  -> {v->1, l->0, o->0} - result = "vlvo"
    5. consume v  -> {v->0, l->0, o->0} - result = "vlvov"

    success : return result when all items are consumed.
    failure : break when same there is only one item and it's same as result's
        last char.

    Algorithm:
        1. put all items in the freq map
        2. build max heap from freq map
        3. until max heap is not empty
            1. pop top item and compare with result last char
                1. if same, save that item and check max_heap,
                    1. if emptry, return ''
                    2. if not empty, pop one more item
                        1. save that item in result
                        2. reduce the freq of that char and push it to max_heap
                2. if not same, update the result
            3.push that item in the max_heap

    """
    # save result
    result = ''

    # create freq map
    freq_map = defaultdict(int)
    for i in s:
        freq_map[i] += 1

    # max heap to store the items based on the max freq
    max_heap = []
    # populate the max heap
    for item in freq_map.items():
        char, freq = item
        heapq.heappush(max_heap, (-freq, char))

    # until max heap is empty
    while max_heap:
        # pop first item
        first_item_freq, first_item_char = heapq.heappop(max_heap)
        # if result is empty and first item is same as result's last item
        if result != '' and result[-1] == first_item_char:
            # if not empty, we know that the second item is not same as result's
            # last char so append to result, reduce the freq and if freq not 0,
            # push the item into the heap.
            if max_heap:
                second_item_freq, second_item_char = heapq.heappop(max_heap)
                result += second_item_char
                second_item_freq += 1
                # if second item freq less than 0, push item back to heap
                if second_item_freq < 0:
                    heapq.heappush(
                        max_heap, (second_item_freq, second_item_char))
            # if empty, result's last char is same as first item's char
            # so we are done.
            else:
                return ''
        # if result is not empty and first item is not same as result's last
        # char, save char and reduce the freq of the first item
        else:
            result += first_item_char
            first_item_freq += 1

        # if freq of the item is less than 0, continue
        if first_item_freq < 0:
            # push first item back to heap.
            heapq.heappush(max_heap, (first_item_freq, first_item_char))

    return result


def rearrange_string_WRONG(s):
    """By just picking in round robin, we would not be rearrange string in
    expected way.
    For ex, "vvvlo" would be arranged -> vlovv way.
    """
    result = ''
    max_heap = []
    freq_map = defaultdict(int)
    for char in s:
        freq_map[char] += 1

    while any(freq_map.values()):
        for char, freq in freq_map.items():
            if freq != 0:
                heapq.heappush(max_heap, (-freq, char))
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            freq_map[char] -= 1
            if result != '' and result[-1] == char:
                return ''
            result += char

    return result


def main():
    print("Rearranged string:  " + rearrange_string("abaab"))
    print("Rearranged string:  " + rearrange_string("babbaa"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("ppaa"))
    print("Rearranged string:  " + rearrange_string("aapa"))
    print("Rearranged string:  " + rearrange_string("vvvlo"))
    print("Rearranged string:  " + rearrange_string(""))
    print("Rearranged string:  " + rearrange_string("abbaabba"))


main()
