"""
-(x < y) will be 0 if x >= y and -1 (i.e. an int with all bits set) if x < y. 

Note that foo & -1 == foo and foo & 0 == 0 for all foo. 

So if x < y, we get y ^ x ^ y, which is equal to x because y ^ y cancels out. 

And otherwise we get y ^ 0, which is y. So we get x if x < y and y otherwise, 
which is exactly what you'd want from a function named min.

For max it's the same thing, except we return y if x < y and x otherwise.
"""


# x & -1 -> x
# x & 0 -> 0

def find_min(x, y):
    return y ^ (x ^ y) & -(x < y)
    #      y ^  x ^ y  & -1  -> y ^ y -> 0
    #      x ^ 0 & -1
    #      x & -1 -> x


def find_max(x, y):
    return x ^ (x ^ y) & -(x < y)
    # x ^  x ^ y & -1  -> x ^ x -> 0
    # y & -1 -> y


print(find_min(10, 20))
print(find_max(10, 20))
