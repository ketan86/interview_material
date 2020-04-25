"""
bunny -> 0 1 2 3 4 5
ears  -> 2
ans   -> 0 2 4 6 8 10
"""


def bunny_ears(n):
    if n == 0:
        return 0

    if n == 1:
        return 2

    return bunny_ears(n - 1) + 2


ears = bunny_ears(100)
print(ears)


"""
bunny -> 0 1 2 3 4 5
ears  -> 0 2 3 2 3 2
ans   -> 0 2 5 7 10 12
"""


def bunny_ears2(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return bunny_ears2(n - 1) + 3
    else:
        return bunny_ears2(n - 1) + 2


ears2 = bunny_ears2(5)
print(ears2)
