#Using List 

class Stack:
	def __init__(self):
		self.items=[]

	
	
	def isEmpty(self):
		return self.items == []

	def push(self,item):
		# Appending the item to the list, I realise that because it is a dynamic array, it will rewrite all the elements to a new location
		# which means it will take O(n) operation
		# amortised cost every time you add element to the cst
		self.items.append(item)

	def pop(self):
		#Popping the last element in the list, i think takes only O(1) operation
		try:
			if self.items != []:
				return self.items.pop()
		except IndexError:
			return None
	def stacklen(self):
		return len(self.items)

	def peek(self):
		try:
			if self.items != []:
				return self.items[len(self.items)-1]
		except IndexError:
			return None


#Using LinkedList

class Node:
	def __init__(self,val = None,next = None):
		self.val = val
		self.next = next

class Stack:
	def __init__(self):






