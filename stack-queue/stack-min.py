class MinStack:
    
    def __init__(self):
        self.q = []

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin));

    def pop(self):
        return self.q.pop() if self.q else None


    # @return an integer
    def top(self):
        return self.q[-1][0] if self.q else None

    # @return an integer
    def getMin(self):
        return self.q[-1][1] if self.q else None