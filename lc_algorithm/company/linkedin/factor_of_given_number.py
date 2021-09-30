"""
write a program to list factors of a given number
e.g. for 12, factors are 1, 2., 3, 4, 6, 12
"""
import math
# O(N)


def find_factors(nums):
    result = []
    for i in range(1, nums + 1):
        if nums % i == 0:
            print('i:', i)
            result.append(i)
    return result

# O(nlogn)


def find_factors(nums):
    result = []
    for i in range(1, int(math.sqrt(nums)) + 1):
        if nums % i == 0:
            print('i:', i)
            result.append(i)
            result.append(nums // i)

    return result


print(find_factors(120))
