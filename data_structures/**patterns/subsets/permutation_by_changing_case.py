"""
Problem Statement #
Given a string, find all of its permutations preserving the character
sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""
# pylint: skip-file


# each char can be arranged in 2! way and digit in 1!
# so for ex, ad52 can be arranged in 2! x 2! x 1! x 1!  = 4 ways
#            ab7c can be arragned in 2! x 2! x 1! x 2! = 8 ways
def find_letter_case_string_permutations(s):
    return _find_permutations(s, 0, '', [])


def _find_permutations(s, index, perm, result):
    # when perm string length matches the actual input string, record the
    # result.
    if len(perm) == len(s):
        result.append(perm)
    else:
        # if current character is not digit, send two combination, else one
        if not s[index].isdigit():
            capital, non_capital = s[index].capitalize(), s[index]
            _find_permutations(s, index + 1, perm + capital, result)
            _find_permutations(s, index + 1, perm + non_capital, result)
        else:
            _find_permutations(s, index + 1, perm + s[index], result)

    return result


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
