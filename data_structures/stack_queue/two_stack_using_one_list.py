import array


class twoStacks:
    def __init__(self, size):
        self.arr = array.array('i')
        self.total_stack1 = 0
        self.total_stack2 = 0

# Insert Value in First Stack
    def push1(self, value):
        self.arr.insert(0, value)
        self.total_stack1 += 1

# Insert Value in Second Stack
    def push2(self, value):
        self.arr.insert(-1, value)
        self.total_stack2 += 1

# Return and remove top Value from First Stack
    def pop1(self):
        if self.total_stack1 == 0:
            return None
        item = self.arr.pop(0)
        self.total_stack1 -= 1
        return item

# Return and remove top Value from Second Stack
    def pop2(self):
        if self.total_stack2 == 0:
            return None
        item = self.arr.pop(-1)
        self.total_stack2 -= 1
        return item
