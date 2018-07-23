class MinStack:
    def __init__(self):
        self.stack =[]

    def push(self,item):
        self.currentMinimum = self.getMinimum()
        print('Push,initial CurrentMinimum',self.currentMinimum)
        if self.currentMinimum is None or item < self.currentMinimum:
            self.currentMinimum = item
        self.stack.append((item,self.currentMinimum))

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[len(self.stack)-1][0]
        return None

    def getMinimum(self):
        if self.peek() is not None:
            return self.stack[len(self.stack)-1][1]
        return None


minstack = MinStack()
minstack.push(-1)
minstack.push(3)
minstack.push(100)
minstack.pop()
minstack.peek()
print(minstack.getMinimum())