a = "hello"
b = "world"

if (a == b):
    print("相等")
else:
    print("不等")

print(0.1 + 0.2 == 0.3)
print(0.1)
print(0.2)
print(0.1 + 0.2)
print(0.3)

# 判断两个数是否相等, 应该要作差去判断
c = 0.1 + 0.2
d = 0.3
# Python支持连续判断小于大于, 但C++/Java不支持连续判断
print(-0.0000001 < (c - d) < 0.0000001)

c, d = d, c # 多元赋值
print(c)
print(d)

# Python不支持++a, a++等其他语言的自增操作
# ++a
# a++