"""
Two sorted list of positive numbers, find out the first k pairs with the
smallest product. each pair contains one number from each list.

Example: [1,3,5,7], [2,4,5,8], k = 2
[1,2] [2,3]

[2,3,5,7], [2,4,5,8]
   ^            ^

4,[1,4]
2,[1,2]

"""


import heapq


def find_k_smallest_pairs(num1, num2, k):
    min_heap = []

    # find all k pairs of one array with first element of second array
    """
    [1,3,5,7], [2,4,5,8], k = 3           
    
    6,i->1, j -> 0
    5,i->0, j -> 2
    10,i->2, j -> 0

    2,i->0, j->0  -> j->1 (4*1)
    
    4,i->0, j->1  -> j->2 (5*1)



    """
    for i in range(min(k, len(num1))):
        product = num1[i] * num2[0]
        heapq.heappush(min_heap, (product, i, 0))

    result = []

    # go until k is greater than 0
    while k > 0:
        # pull the min product element
        # NOTE: first element will always be minimum and rest will be replaced
        # when new element is added in min_heap
        _, i, j = heapq.heappop(min_heap)

        # using the index, push it to result
        result.append([num1[i], num2[j]])

        # go over the second array and put the product in the min_heap
        if j + 1 < len(num2):
            product = num1[i] * num2[j+1]
            heapq.heappush(min_heap, (product, i, j+1))
        k -= 1

    return result


print(find_k_smallest_pairs([1, 3, 5, 7], [2, 4, 5, 8], k=2))
