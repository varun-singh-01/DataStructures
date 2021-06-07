class Stack():
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.maz_size == self.size

    def push(self, item):
        if self.isFull():
            raise Exception("Error: Stack is Full!")

        self.stack.append(item)
        self.size += 1

    def pop(self, item):
        if self.isEmpty():
            raise Exception("Error: Stack is Empty!")

        self.stack.pop()
        self.size -= 1

    def top(self, item):
        if self.isEmpty():
            raise Exception("Error: Stack is Empty!")

        return self.stack[self.size - 1]

    def size(self):
        return self.size

    def list_items(self):
        for i in self.stack:
            print(i)


if __name__ == '__main__':

    # Create Stack
    my_stack = Stack(5)

    # Insert
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(5)

    # List
    my_stack.list_items()

    # Remove Items
    my_stack.pop()

    # List
    my_stack.list_items()
