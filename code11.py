def isOdd(num):
    if num % 2 != 0:
        return True
    return False


print(isOdd(10))
print(isOdd(11))


# Python的函数可以一次返回多个值
def getPoint():
    x = 10
    y = 20
    z = 30
    return x, y, z


# 可采用多元赋值接收多个返回值
a, b, c = getPoint()
print(f"a = {a}, b = {b}, c = {c}")

# 对于不需要关心的返回值可以使用下划线进行代替接收多个返回值
_, b, c = getPoint()
print(f"b = {b}, c = {c}")

num = 10


def test():
    global num # 声明num为全局变量
    num = 20


test()
print(num)

for i in range(1, 11):
    print(i)

print("--------------")
# Python中也可以访问到for循环中的变量i
print(i)

# 在Python中只有函数和类才会涉及到作用域的问题


