"""
Binary search tree implementation.
"""
# pylint: skip-file


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = TreeNode(data)

    def search(self, data):
        if data < self.data:
            if self.left is None:
                return False
            return self.left.search(data)
        elif data > self.data:
            if self.right is None:
                return False
            return self.right.search(data)
        else:
            return True

    def delete(self, data):
        # if value is less than the current node value, go left
        if data < self.data:
            # if left node is present
            if self.left:
                # KEY => set the values of returned node to left node.
                # It means, the `else` condition must return the node
                # that should be set as either left or right node of
                # the current node.
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            # if both left and right child of the current node is none,
            # we can safely remove the current node and return the none,
            # so parent node can set left/right node to none to detach
            # the node.
            if self.left is None and self.right is None:
                return None

            # if left node is none, only return the right node
            elif self.left is None:
                return self.right
            # if right node is none, only return the left node
            elif self.right is None:
                return self.left
            # if both nodes are not none, we need to find min of the right
            # sub tree or max of the left sub tree.
            else:
                # find the min of the right sub tree
                curr = self.right
                # go all the way left
                while curr.left:
                    curr = curr.left
                # set min left node value to current first
                self.data = curr.data
                # go and delete the min left node
                self.right = self.right.delete(curr.data)

        # return current node, in `else or else` switched the nodes so current
        # node should be set to current node.
        return self

    def pre_order(self):  # root -> left -> right
        if self is not None:
            print(self.data)
            if self.left is not None:
                self.left.pre_order()
            if self.right is not None:
                self.right.pre_order()

    def in_order(self):  # left -> root -> right
        if self is not None:
            if self.left is not None:
                self.left.in_order()
            print(self.data)
            if self.right is not None:
                self.right.in_order()

    def post_order(self):  # left -> right -> root
        if self is not None:
            if self.left is not None:
                self.left.post_order()
            if self.right is not None:
                self.right.post_order()
            print(self.data)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root.insert(data)

    def search(self, data):
        if self.root is None:
            return False
        return self.root.search(data)

    def delete(self, data):
        if self.root is None:
            return False
        return self.root.delete(data)

    def pre_order(self):
        if self.root is not None:
            self.root.pre_order()

    def in_order(self):
        if self.root is not None:
            self.root.in_order()

    def post_order(self):
        if self.root is not None:
            self.root.post_order()


bst = BinarySearchTree()
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(8)
bst.insert(2)
bst.insert(1)
print(bst.search(9))
print(bst.in_order())
print(bst.pre_order())
print(bst.post_order())
