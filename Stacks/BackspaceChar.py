def backspaceCompare( S, T):
    stack_S =[]
    stack_T =[]
    string_S = ""
    string_T = ""

    if len(S) == 0 and len(T) == 0:
        return True


    for i in range(0,len(S)):
        if S[i] != '#':
            stack_S.append(S[i])
        if S[i] == '#':
            stack_S.pop()

    for i in range(0,len(T)):
        if T[i] != '#':
            stack_T.append(T[i])
        if T[i] == '#':
            stack_T.pop()
    print(stack_T,stack_S)

    count = min(len(stack_S),len(stack_T))

    while count > 0:
        if stack_S[-1] == stack_T[-1]:
            stack_S.pop(),stack_T.pop()
        count = count-1

    return len(stack_S) == 0 and len(stack_T) == 0

S = "ab#c"
T = "ad#c"

print(backspaceCompare(S,T))

