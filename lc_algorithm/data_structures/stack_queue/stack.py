class Stack:
    def __init__(self):
        self.stackList = []

    def isEmpty(self):
        return len(self.stackList) == 0

    def top(self):
        if self.isEmpty():
            return None
        return self.stackList[-1]

    def size(self):
        return len(self.stackList)

    def push(self, value):
        self.stackList.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stackList.pop()

    def __repr__(self) -> str:
        return str(self.stackList)

    def print(self):
        print(self.stackList)

# stack = Stack()
# for i in range(5):  # Pushing values in
#     stack.push(i)

# print("top(): " + str(stack.top()))

# for x in range(5):  # Removing values
#     print(stack.pop())

# print("isEmpty(): " + str(stack.isEmpty()))  # Checking if its empty
