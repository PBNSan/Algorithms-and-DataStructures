#Considering the top of the stack is the right most element of the list

# class Stack:
# 	def __init__(self):
# 		self.items=[]

# 	def isEmpty(self):
# 		return (True if self.items == [] else False)

# 	def push(self,item):
# 		self.items.append(item)

# 	def pop(self):
# 		self.items.pop()

# 	def stacklen(self):
# 		return len(self.items)

# 	def peek(self):
# 		return self.items[len(self.items)-1]



# Considering the top of the stack is the left most element in the list

class Stack:
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items == []

	def push(self,item):
		self.items.insert(0,item)

	def pop(self):
		self.items.pop(0)

	def stacklen(self):
		return len(self.items)

	def peek(self):
		return self.items[0]


stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
stack.pop()
print('length of stack', stack.stacklen())
print('stack items',stack.items)
print('stack peek- top most element in the stack',stack.peek())
print('Is stack empty?',stack.isEmpty())