"""
Given two Binary Trees, write a function that returns true if two trees are 
mirror of each other, else false. For example, the function should return true 
for following input trees.


For two trees ‘a’ and ‘b’ to be mirror images, the following three conditions 
must be true: 
 

Their root node’s key must be same
Left subtree of root of ‘a’ and right subtree root of ‘b’ are mirror.
Right subtree of ‘a’ and left subtree of ‘b’ are mirror.
Below is implementation of above idea. 
 
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def are_mirror(a, b):
    if not a and not b:
        return True

    if not a or not b:
        return False

    return (
        a.data == b.data and
        are_mirror(a.left, b.right) and
        are_mirror(a.right, b.left)
    )


# Driver code
root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(4)
root2.right.right = Node(5)

if are_mirror(root1, root2):
    print("Yes")
else:
    print("No")
