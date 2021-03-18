"""
Any number will be called a happy number if, after repeatedly replacing it with
a number equal to the sum of the square of all of its digits, leads us to
number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they
will be stuck in a cycle of numbers which does not include ‘1’.
"""
# pylint: skip-file

# simple way to determine cycle. space complexity


def find_happy_number(num):
    square_sum = set()
    while True:
        ss = 0
        for i in str(num):
            ss += int(i) * int(i)
        if ss == 1:
            return True
        if ss in square_sum:
            return False
        square_sum.add(ss)
        num = ss
    return False

# slow and fast pointer
# happy number has an end "1" and slow and fast pointer will meet at 1.
# unhappy numbers has no end and slow and fast pointer will meet at some point
# other than 1.


def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = _find_square_sum(slow)
        fast = _find_square_sum(_find_square_sum(fast))
        if slow == fast:
            break
    return slow == 1


def _find_square_sum(num):
    _sum = 0
    while (num > 0):
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


def main():
    print(find_happy_number(4))
    print(find_happy_number(12))


main()
