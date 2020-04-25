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


def evaluatePostFix(exp):
    operators = {
        '*': 'mul',
        '+': 'sum',
        '-': 'sub',
        '/': 'div'
    }
    stack = myStack()

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
    stack = myStack()
    for char in exp:
        if char.isdigit():
            stack.push(char)
        else:
            right = stack.pop()
            left = stack.pop()
            stack.push(str(eval(left + char + right)))
    return int(float(stack.pop()))


print("Result: " + str(evaluatePostFix("921*-8-4+")))
