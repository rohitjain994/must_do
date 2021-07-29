class MyStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = collections.deque([])

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)

    # @return nothing
    def pop(self):
        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

        return self.stack.popleft()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0