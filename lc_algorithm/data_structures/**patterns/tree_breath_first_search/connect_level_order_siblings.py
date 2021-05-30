"""
Given a binary tree, connect each node with its level order successor.
The last node of each level should point to a null node.
"""
# pylint: skip-file
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    # if root is None, return
    if root is None:
        return
    # use deque and add root
    queue = deque()
    queue.append(root)
    # loop until queue is empty
    while queue:
        # find the total nodes at each level
        total_nodes = len(queue)
        # define prev node
        prev = None
        # pop each node
        for i in range(total_nodes):
            node = queue.popleft()
            # if prev node is not None
            if prev:
                prev.next = node
            prev = node
            # insert left first and right later
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)
    # connect_level_order_siblings_2(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
