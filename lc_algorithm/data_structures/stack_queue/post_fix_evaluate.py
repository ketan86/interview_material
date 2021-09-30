"""
The usual convention followed in mathematics is the infix expression.
Operators like + and * appear between the two numbers involved in the
calculation:

6 + 3 * 8 - 4
Another convention is the postfix expression where the operators appear
after the two numbers involved in the expression. In postfix, the expression
written above will be presented as:

6 3 8 * + 4 -
The two digits preceding an operator will be used with that operator

From the first block of digits 6 3 8, we pick the last two which are 3 and 8.
Reading the operators from left to right, the first one is *. The expression
now becomes 3 * 8
The next number is 6 while the next operator is +, so we have 6 + 8 * 3.
The value of this expression is followed by 4, which is right before -. Hence
we have 6 + 8 * 3 - 4.
Implement a function called evaluatePostFix() that will compute a postfix
expression given to it as a string.

Input #
A string containing a postfix mathematic expression. Each digit is considered
to be a separate number, i.e., there are no double digit numbers.

Output #
A result of the given postfix expression.

Sample Input #
exp = "921*-8-4+" # 9 - 2 * 1 - 8 + 4

Sample Output #
3
"""
# pylint: skip-file
import pdb
from stack import Stack


def evaluatePostFix(exp):
    operators = {
        '*': 'mul',
        '+': 'sum',
        '-': 'sub',
        '/': 'div'
    }
    stack = Stack()

    for i in exp:
        if i in operators:
            first = stack.pop()
            second = stack.pop()
            if operators[i] == 'mul':
                stack.push(second * first)
            elif operators[i] == 'sum':
                stack.push(second + first)
            elif operators[i] == 'sub':
                stack.push(second - first)
            elif operators[i] == 'div':
                stack.push(second / first)
        else:
            stack.push(int(i))

    return stack.pop()


# other option using "eval"

def evaluatePostFix(exp):
    stack = Stack()
    # loop over the expression
    for char in exp:
        # add digits to stack until operator is found
        if char.isdigit():  # NOTE: Does not work for "-11" if given as whole
            # as integer
            # Here it works because it's a string input but
            # ["10","-11","*"] does not work so check if operator
            # else consider digit.
            stack.push(char)
        else:
            # pop last two items and evaluate the results
            # push the results to stack.

            # KEY -> pop items first before using it in the
            # eval because the order in which items are popped
            # matter. Directly using it in eval cause items
            # to pop in different order.

            # 84-    -> [8, 4]
            #           right => 4
            #           left => 8
            #           left - right => 4

            right = stack.pop()
            left = stack.pop()

            # push evaluated values back to stack.
            # eval only works with string so convert
            # results back to string.
            # (Pdb) str(eval(left + char + right))
            # '2'
            # (Pdb) eval(left + char + right)
            # 2
            # (Pdb) left
            # '2'
            # (Pdb) right
            # '1'
            # (Pdb) char
            # '*'
            stack.push(str(eval(left + char + right)))

    return int(float(stack.pop()))


print("Result: " + str(evaluatePostFix("921*-8-4+")))
