#Using List
def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    list_0 = []
    for i in ops:
        if i not in ['C','D','+']:
            list_0.append(int(i))
            print(list_0)
        if i == 'C':
            list_0 = list_0[:-1]
            print(list_0)
        if i == 'D':
            val = list_0[-1] * 2
            list_0.append(int(val))
            print(list_0)
        if i == '+':
            val = list_0[-1] + list_0[-2]
            list_0.append(int(val))
            print(list_0)

    print(sum(list_0))
    return sum(list_0)





ops = ["5","2","C","D","+"]

calPoints(ops)