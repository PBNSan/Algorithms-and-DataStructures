# stack {
# 	void push()
# 	int pop()
# 	int peek()
# 	bool isEmpty();
# }

# index = -1, 0, 1, 2, 3
# # 


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



maxSize = 10
stack = Stack(maxSize)

for i in range(0,maxSize):
	if i % 2 == 0:
		print('Popping val',stack.peek())
	else:
		stack.push(i)

# for i in range(0,maxSize):
# 	print(stack.peek())
# 	print('Popping', stack.pop())




