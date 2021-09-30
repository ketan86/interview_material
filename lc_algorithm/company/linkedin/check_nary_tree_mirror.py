"""
Given a Tree where every node contains variable number of children, convert the
tree to its mirror. Below diagram shows an example.


Node of tree is represented as a key and a variable sized array of children
pointers. The idea is similar to mirror of Binary Tree. For every node,
we first recur for all of its children and then reverse array of children 
pointers. We can also do these steps in other way, i.e., reverse array of 
children pointers first and then recur for children.

Below is C++ implementation of above idea.
"""


class Node:

    # Utility function to create a new tree node
    def __init__(self, data):
        self.data = data
        self.child = []


def are_mirror(a, b):
    # if no child, return True
    if not a and not b:
        return True

    # if one has child and other does not, return False
    if not a or not b:
        return False

    # if length of the child is diff, return False
    if len(a.child) != len(b.child):
        return False

    # check if all child are mirror
    all_mirror = True
    for ac, bc in zip(a.child, list(reversed(b.child))):
        all_mirror = all_mirror and are_mirror(ac, bc)

    # if root is same and all child are mirror, return True else
    # false
    return (
        a.data == b.data and all_mirror
    )


root1 = Node(10)
root1.child.append(Node(2))
root1.child.append(Node(34))
root1.child.append(Node(56))
root1.child.append(Node(100))
root1.child[2].child.append(Node(1))
root1.child[3].child.append(Node(7))
root1.child[3].child.append(Node(8))
root1.child[3].child.append(Node(9))


#   *              10
#     *        /   /    \   \
#     *        2  34    56   100
#     *                 |   /  | \
#     *                 1   7  8  9

#   *              10
#     *        /   /    \   \
#     *      100  56   34   2
#     *     / | \  |
#     *    9  8  7 1

root2 = Node(10)
root2.child.append(Node(100))
root2.child.append(Node(56))
root2.child.append(Node(34))
root2.child.append(Node(2))
root2.child[0].child.append(Node(9))
root2.child[0].child.append(Node(8))
root2.child[0].child.append(Node(7))
root2.child[1].child.append(Node(1))

print(are_mirror(root1, root2))
