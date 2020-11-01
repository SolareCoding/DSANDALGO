def fabonacci(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return fabonacci(index - 2) + fabonacci(index - 1)

def fabonacci_tail(index, lastTwoElement, lastOneElement):
    if index == 0:
        return lastTwoElement
    return fabonacci_tail(index - 1, lastOneElement, lastOneElement + lastTwoElement)

def callSelf(index, sum):
    if index == 0:
        return sum
    return callSelf(index - 1, sum + 2)

def noRecursion(index, sum):
    while index > 0:
        sum = sum + 2
        index = index - 1
    return sum

if __name__ == "__main__":
    print(fabonacci(2))
    print(fabonacci_tail(2, 0, 1))
