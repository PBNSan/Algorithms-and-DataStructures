class Stack:
	def __init__(self, maxSize = 5):
		self.items = [None] * maxSize
		self.maxSize = maxSize
		self.curIndex = -1

	def isEmpty(self):
		return self.curIndex == -1

	def isFull(self):
		return self.curIndex == self.maxSize - 1

	def push(self,item):
		if not self.isFull():
			self.items[self.curIndex+1] = item
			self.curIndex += 1
		else:
			print('Index out of range')

	def pop(self):
		if not self.isEmpty():
			pop_element = self.items[self.curIndex]
			self.curIndex = self.curIndex-1
			return pop_element
		else:
			print('stack is empty')

	def peek(self):
		if not self.isEmpty():
			return self.items[self.curIndex]
		else:
			print('stack is empty')


class MaxStack:
    def __init__(self):
        self.stack=Stack()
        self.max_stack=Stack()

    def push(self,item):
        print('Call to Push')
        self.stack.push(item)
        print('Pushing to Stack',item)
        print(item >= self.max_stack.peek())
        print(self.max_stack.isEmpty())
        if self.max_stack.isEmpty() or item >= self.max_stack.peek():
            print('Pushing to MaxStack',item)
            self.max_stack.push(item)

    def pop(self):
        print('Call to pop')
        item = self.stack.pop()
        print('popping from stack',item)
        if item == self.max_stack.peek():
            self.max_stack.pop()
            print('popping from max stack',item)
        return item

    def maxElement(self):
        print('Returning largest Element in stack',self.max_stack.peek())
        return self.max_stack.peek()



maxStack = MaxStack()
maxStack.push(2)
maxStack.push(3)
maxStack.push(3)
maxStack.push(10)
maxStack.push(2)
maxStack.pop()
maxStack.pop()
#maxStack.push(100)
maxStack.maxElement()