"""
Any number will be called a happy number if, after repeatedly replacing it with
a number equal to the sum of the square of all of its digits, leads us to number
‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be
stuck in a cycle of numbers which does not include ‘1’.


In number theory, a happy number is a number which eventually reaches 1 when
replaced by the sum of the square of each digit. 

For instance, 13 is a happy number because 
    1^2 + 3^2 = 10 and
    1^2 + 0^2 =  1  

On the other hand, 4 is not a happy number because the sequence starting with  \
    4^2 = 16
    1^2 + 6^2 = 37 eventually reaches  \
    2^2 + 0^2 = 4 

the number that started the sequence, and so the process continues in an 
infinite cycle without ever reaching 1.
A number which is not happy is called sad or unhappy.

"""
# pylint: skip-file

# simple way to determine cycle. space complexity


def find_happy_number(num):
    """
    Runtime: 36 ms, faster than 56.33%

    Non-happy numbers repeat whereas happy numbers reaches 1 without any
    repetition.

    Keep summing numbers' digits until num is found in the num set. if found
    return False else check if number is 1.
    """
    # save square in the set
    num_set = set()

    # until number is greater than 1 and not found in set
    while num > 1 and num not in num_set:
        # add num in set
        num_set.add(num)
        # sum current number's digits
        num = sum([int(i) * int(i) for i in str(num)])

    # to handle when number becomes 1 and found in num_set
    return num == 1


def find_happy_number(num):
    """
    Using slow and fast pointer
        - happy number has an end "1" and slow and fast pointer will meet at 1.
    unhappy numbers has no end and slow and fast pointer will meet at some point
    other than 1.

    Happy Number: 19
        19 -> 82 -> 68 -> 100 -> 1 
                    s            f

    Non-Happy Number: 2
        2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20
                                           s                                               f

    Happy number will end at 1 and fast pointer will be stuck at 1 until slow
    pointer reaches fast pointer and when they meet, either it's 1 or some
    other number if there is a loop.

    """
    # slow and fast pointers
    slow, fast = num, num
    # loop until slow and fast pointers meet
    while True:
        # move slow pointer by one
        slow = _find_square_sum(slow)
        # move fast pointer by two
        fast = _find_square_sum(_find_square_sum(fast))
        # if slow and fast pointers meet, break
        if slow == fast:
            break
    # if slow pointer is at 1, it's happy number else not
    return slow == 1


def _find_square_sum(num):
    # find sum of by squaring number's digits
    _sum = 0
    while (num > 0):
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


def main():
    print(find_happy_number(19))
    print(find_happy_number(12))


main()
