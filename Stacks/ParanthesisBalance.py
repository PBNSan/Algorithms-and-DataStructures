def isValid(ip):
    stack = []
    for i in range(0,len(ip)):
        top = len(stack)-1
        if ip[i] == '[' or ip[i] == '{'  or ip[i] =='(':
            stack.append(ip[i])
        elif top < 0:
            return False
        elif (stack[top] == '[' and ip[i] == ']') or (stack[top] == '{' and ip[i] =='}') or (stack[top] == '(' and ip[i] == ')'):
            stack.pop()
        else:
            return False

    if len(stack) > 0:
        return False

    return True


ip = ']'
print(isValid(ip))