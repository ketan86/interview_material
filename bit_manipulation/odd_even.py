def find_even_odd_AND(n):

    # if result of n AND 1 is 1, it's odd else even
    if n & 1:
        return 'odd'
    return 'even'


def find_even_odd_XOR(n):

    # if results of n XOR 1 is less than n, its odd
    # 1100(12) -> 1100 ^ 1 = 1101(13) -> even
    # 1011(11) -> 1011 ^ 1 = 1010(10) -> odd
    if (n ^ 1) < n:
        return 'odd'
    return 'even'


print(find_even_odd_AND(11))
print(find_even_odd_XOR(11))
