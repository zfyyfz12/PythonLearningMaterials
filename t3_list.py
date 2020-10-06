# 列表属于可变类型，能改
list1 = ['a', 'b', 'c']
print(list1[1])

print(list1.index('a', 0, 2))

print(list1.count('a'))

print(len(list1))

print('a' in list1)
print('d' not in list1)

# 增
list1.append('d')
list1.append([11, 12])  # 整个追加 输出['a', 'b', 'c', 'd', [11, 12]]
list1.extend('efg')  # 拆开追加['a', 'b', 'c', 'd', [11, 12], 'e', 'f', 'g']
list1.insert(0, 'z')
print(list1)

# 删
# del list1 #删除整个列表
del list1[0]
print(list1)
print(list1.pop())  # 默认删除最后一个元素并返回
print(list1.pop(0))  # 删除制定下标元素，并返回
print(list1)

list1.remove('b')
print(list1)

list1.clear()
print(list1)

# 改
b = [1, 2, 3, 4, 5]
b[0] = 100

print(b)
b.reverse()
print(b)

b.sort()  # 默认升序排序
print(b)
b.sort(reverse=True)  # 降序排序
print(b)

# 复制
nb = b.copy()
print(nb)

# 遍历
i = 0
while i < len(b):
    print(b[i])
    i += 1

for i in b:
    print(i)

# 列表嵌套
c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(c[0][0])
