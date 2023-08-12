# 函数
def calSum(begin, end):
    theSum = 0
    for i in range(begin, end + 1):
        theSum += i
    print(theSum)


# 期望有两个空行在函数或类的后边
calSum(1, 100)
calSum(300, 400)
calSum(1, 1000)


def add(x, y):
    return x + y


print(add(10, 20))
print(add("hello ", "world"))
