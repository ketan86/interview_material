"""
Given a binary tree, return an array containing all the boundary nodes
of the tree in an anti-clockwise direction.

The boundary of a tree contains all nodes in the left view, all leaves,
and all nodes in the right view. Please note that there should not be
any duplicate nodes. For example, the root is only included in the left
view; similarly, if a level has only one node we should include it in
the left view.


          1
        /  \
      2      3
    /  \    /  \
   4   5   6   7
  / \  |   |   / \
 8  9  10  11 12 13
 [1, 2, 4, 8, 9, 10, 11, 12,13, 7, 3]
"""
# pylint: skip-file
from collections import deque
import pdb


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_tree_boundary(root):
    """
    # NOTE: Does not cover all testcases

                1
                  \ 
                    2   
                  /  \
                 3   4

            1,3,4,2 instead of 1,2,3,4      
    """
    # main result list to store top to bottom left and bottom left to right
    # elements. for ex, 1,2,4,8,9,10,11,12,13
    result = []
    # right view results to store right side top to bottom elements.
    # for ex, 7, 3 - we use deque to append on left so get right bottom
    # up access.
    rv_result = deque()

    if not root:
        return result
    queue = deque()
    queue.append(root)

    while queue:
        level_nodes = len(queue)
        for i in range(level_nodes):
            node = queue.popleft()
            # if we encounter leaf node.
            if node.left is None and node.right is None:
                # decide if it should be pushed back to queue or be saved in
                # results based on if there are any node ahead of the current
                # with child.

                # If the len of the queue only contains the nodes that are in
                # current level, add the node into result else back in queue.
                """
                                                 12
                                             /       \
                                            7           1
                                         /    \     /      \
                                        4      3   10        5
                                     /    \    |   |        /
                                    9      15  3   10      6
                                 /  \      |   |   |       |
                               13    14    15  3   10      6

                at node 3, we found a leaf node but number of nodes at level 3
                already contains node 9 and node 15 so queue length wont be
                equal to total nodes - current node. If not, push element to
                queue. so current node list would be,
                    [10, 5, 9, 15, 3]
                    [5, 9, 15, 3, 10]
                    [9, 15, 3, 10, 6]


                    [3,10,5,9,15]
                """
                # only last level would not add any more nodes to queue so
                # length of the queue would be equal to current node to end.
                if len(queue) == level_nodes - (i + 1):
                    result.append(node)
                else:
                    queue.append(node)
            else:
                # if it is a first node, it goes in result. starting from
                # first top left to bottom left, all first elements at each
                # level goes in result.
                if i == 0:
                    result.append(node)
                # all last nodes starting from second level to n-1 level,
                # goes in right view result appended in front of the list.
                elif i == level_nodes - 1:
                    rv_result.appendleft(node)

            # if there are left or right nodes, append them in queue.
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # move all right view elements stored in bottom up manner, push
    # them in result list.
    if rv_result:
        result.extend(rv_result)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(9)
    root.left.left.left.left = TreeNode(13)
    root.left.left.left.right = TreeNode(14)
    root.left.right = TreeNode(3)
    root.left.left.right = TreeNode(15)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(6)
    result = find_tree_boundary(root)
    print("Tree boundary: ", end='')
    for node in result:
        print(str(node.val) + " ", end='')

    """
                         12
                      /       \
                    7           1
                 /    \     /      \
                4      3   10        5
              /      /             /
            9      15             6
          /  \
         4    3

    """

    # root = TreeNode(12)
    # root.right = TreeNode(1)
    # root.right.left = TreeNode(10)
    # root.right.right = TreeNode(5)
    # result = find_tree_boundary(root)
    # print("\nTree boundary: ", end='')
    # for node in result:
    #     print(str(node.val) + " ", end='')

    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.left.left = TreeNode(8)
    # root.left.left.right = TreeNode(9)
    # root.left.right = TreeNode(5)
    # root.left.right.right = TreeNode(10)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # root.right.left.left = TreeNode(11)
    # root.right.right.left = TreeNode(12)
    # root.right.right.right = TreeNode(13)
    # result = find_tree_boundary(root)
    # print("\nTree boundary: ", end='')
    # for node in result:
    #     print(str(node.val) + " ", end='')
    # print()


main()
