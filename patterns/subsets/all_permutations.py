"""
Problem Statement #
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set.
For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]


"""
# pylint: skip-file
from collections import deque

# iterative solution


def find_permutations(nums):
    perm_size = len(nums)
    result = []
    queue = deque()
    queue.append([])

    for num in nums:
        count = len(queue)
        for i in range(count):
            perm = queue.popleft()
            # add num in all positions of current permutation and create
            # those many distinct new permutation

            # since we have to add a number to both sides of the number, we
            # need to go one step extra.
            # for ex, to add 3 to [1,2], we have to loop two times and insert
            # 3 at 0, 1 and 2 positions since len(perm) + 1
            for j in range(len(perm) + 1):
                new_perm = list(perm)
                new_perm.insert(j, num)
                queue.append(new_perm)
                # we only register a result when len of the new_perm meets
                # actual perm size of the input array. means when we are at
                # last level during BFS.
                if len(new_perm) == perm_size:
                    result.append(new_perm)
    return result

# recursive


def find_permutations_recursive(nums):
    return _generate_perms(nums, perm=[], result=[], index=0)


def _generate_perms(nums, perm, result, index):
    # until the length of the perm is same as length of the nums,
    # keep creating permutations.
    if len(perm) == len(nums):
        result.append(perm)
    else:
        for i in range(len(perm) + 1):
            new_perm = list(perm)
            new_perm.insert(i, nums[index])
            _generate_perms(nums, new_perm, result, index + 1)

    return result


def main():
    print("Here are all the permutations (I): " +
          str(find_permutations([1, 3, 5])))

    print("Here are all the permutations (R): " +
          str(find_permutations_recursive([1, 3, 5])))


main()
