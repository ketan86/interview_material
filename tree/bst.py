class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data > self.data:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)

    def preorder(self):
        if self is not None:
            print(self.data)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self is not None:
            if self.left:
                self.left.inorder()
            print(self.data)
            if self.right:
                self.right.inorder()

    def postorder(self):
        if self is not None:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.data)

    def search(self, data):
        if self is not None:
            if data == self.data:
                return True
            if self.left:
                return self.left.search(data)
            if self.right:
                return self.right.search(data)
        return False

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if not self.left and not self.right:
                return None
            elif not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                # find min in right sub tree
                curr = self.right
                # go all the way left
                while curr.left:
                    curr = curr.left
                # set min left node value to current first
                self.data = curr.data
                # go and delete the min left node
                self.right = self.right.delete(curr.data)
        return self


class BST:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root.insert(data)

    def preorder(self):
        # root -> left -> right
        if self.root:
            self.root.preorder()

    def inorder(self):
        # left -> root -> right
        if self.root:
            self.root.inorder()

    def postorder(self):
        # left -> right -> root
        if self.root:
            self.root.postorder()

    def search(self, data):
        if self.root:
            return self.root.search(data)

    def delete(self, data):
        if self.root:
            self.root = self.root.delete(data)


bst = BST(6)
bst.insert(4)
bst.insert(2)
bst.insert(5)
bst.insert(9)
bst.insert(8)
bst.insert(12)
# bst.preorder()
bst.inorder()
# bst.postorder()
