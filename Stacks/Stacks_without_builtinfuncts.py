class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def push(self,item):
		push_index = len(self.items)
		self.items[push_index:] = [item]

	def pop(self):
		try:
			if len(self.items) != 0 :
				last_index = len(self.items)
				self.items = self.items[:last_index-1]
				return self.items
		except IndexError:
			return None

	def peek(self):
		try :
			if len(self.items) != 0:
				return self.items[len(self.items) -1 ]
		except IndexError:
			return None


stack = Stack()

print(stack.isEmpty())
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.items)
print('--Pop--')
stack.pop()
print('------')

print(stack.items)
print(stack.peek())