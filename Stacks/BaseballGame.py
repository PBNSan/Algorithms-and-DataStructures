
def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    stack = []
    stack_1 = []
    sum = 0
    for i in ops:
        if i not in ["C", "D", "+"]:
            if len(stack) != 0:
                sum = stack[-1][1] + int(i)
                stack.append((i, sum))
            else:
                sum = 0 + int(i)
                stack.append((i,sum))
            print(stack)
        if i == "C":
            stack.pop()
        if i == "D":
            print(stack)
            this_round_score = int(stack[-1][0]) * 2
            sum = this_round_score + stack[-1][1]
            stack.append((this_round_score,sum))
            print(stack)
        if i == "+":
            if len(stack) >= 2:
                this_round_score  = 0
                for i in range(0,2):
                    stack_1.append(stack.pop())
                    this_round_score =  this_round_score + int(stack_1[-1][0])
                print(stack_1)
                for i in range(0,2):
                    stack.append(stack_1.pop())
                sum = stack[-1][1] + this_round_score
                stack.append((this_round_score,sum))
                print(stack)



    return stack[-1][1]



ops = ["1","C","-62","-45","-68"]

calPoints(ops)