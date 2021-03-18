"""
Problem Statement #
For a given number ‘N’, write a function to generate all combination of
‘N’ pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

# pylint: skip-file


def generate_valid_parentheses(num):
    return _traverse(num, '(', result=[])


def _traverse(num, s, result):
    # if length of the string is double the num, we found the parentheses
    # but need to check if they are balanced or not.
    if len(s) == num * 2:
        if _is_balanced(s):
            result.append(s)
    else:
        # append left parentheses and right parentheses to each string and
        # keep calculating.
        _traverse(num, s + '(', result)
        _traverse(num, s + ')', result)

    return result


def _is_balanced(s):
    stack = []
    for i in s:
        if '(' == i:
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False

    return True

# Optimized


def generate_valid_parentheses_optimized(num):
    return _traverse_optimized(
        num, '(', result=[], open_p_count=1, close_p_count=0)


def _traverse_optimized(num, s, result, open_p_count, close_p_count):
    if len(s) == num * 2:
        result.append(s)
    else:
        if open_p_count < num:
            _traverse_optimized(
                num, s + '(', result, open_p_count + 1, close_p_count)
        # add until close parent count is less than open.
        # for ex, num is a number of doors. open and close actions are
        # idependent but you can not close the door if there is none open.
        # or in other words, close door count should be less than open.
        # if there are 2 doors open, you can close up to max 2 door but
        # not more.
        # so, ())( -> not valid since we open a door, closed a door and then
        # tried to close the door where no doors were open.
        if close_p_count < open_p_count:
            _traverse_optimized(num, s + ')', result,
                                open_p_count, close_p_count + 1)

    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))

    print("All combinations of balanced parentheses are: (O) : " +
          str(generate_valid_parentheses_optimized(2)))
    print("All combinations of balanced parentheses are: (O) : " +
          str(generate_valid_parentheses_optimized(3)))


main()
