"""
Find number of 1's in an interger.
"""
# pylint: skip-file

def find_num_of_1s(n):
    count = 0
    while n > 0:
        # or count += n % 2
        # last bit AND
        count += n & 1
        n >>= 1

    return count


"""
For ex, n is 7

10110 -> 22
    10110 & 1 = 0, count 0
    10110 >> 1 = 1011    (right shift removes left significant bit(right most))
1011 -> 11
    1011 & 1 = 1, count 1
    1011 >> 1 = 101
101 -> 5
    101 & 1 = 1, count 2
    101 >> 1 = 10
10 -> 2
    10 & 1 = 0, count 2
    10 >> 1 = 1
1 -> 1
    1 & 1 = 1, count 3
    1 >> 1 = 0
"""

print(find_num_of_1s(7))
print(find_num_of_1s(4))
print(find_num_of_1s(78))
print(find_num_of_1s(8))