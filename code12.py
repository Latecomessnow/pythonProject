# a = [1, 2, 3, 4]
# print(a)
# print(a[1:-1])
#
# a[1] = 100
# print(a)
# print(a[::2])

# for循环遍历列表
a = [1, 2, 3, 4]
for elem in a:
    print(elem)
# while循环遍历
b = [1, 2, 3, 4, 5]
i = 0
while i < len(b):
    print(b[i])
    i += 1

a.append(5)
a.append("hello")
print(a)
a.insert(len(a) - 1, "world")
print(a)

print(1 in a)
print(10 in a)
print(1 not in a)
print(10 not in a)
print(a.index(2))
print(a.index(10)) # Python会直接抛异常
