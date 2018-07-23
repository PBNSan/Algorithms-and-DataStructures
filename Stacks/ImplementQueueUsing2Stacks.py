class Queuewith2Stacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack =[]


    def enqueue(self,item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                old_item = self.in_stack.pop()
                self.out_stack.append(old_item)
        return self.out_stack.pop()

    def peek(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                old_item = self.in_stack.pop()
                self.out_stack.append(old_item)
        return self.out_stack[-1]


queue = Queuewith2Stacks()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(4)
#print('dequeu1',queue.dequeue())
queue.enqueue(5)
#print('dequeu2',queue.dequeue())
queue.enqueue(3)
#print('dequeu3',queue.dequeue())

print(queue.peek())

