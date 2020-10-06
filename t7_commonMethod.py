str1 = 'abc'
str2 = 'def'
l1 = [1, 2, 3, 3]
l2 = [4, 5, 6, 6]
t1 = (1, 2, 3)
t2 = (4, 5, 6)
d1 = {'a': 1, 'b': 2}
# + 合并 字典不支持+
print(str1 + str2)
print(l1 + l2)
print(t1 + t2)

# *复制 字典不支持*
print(str1 * 5)
print(l1 * 5)
print(t1 * 5)

print('a' in d1)
print(1 in d1)
print(1 not in d1)
print(1 in d1.values())

# del 目标 或del(目标)

# max() min()
print(max(str1))
print(max(d1))
print(max(d1.values()))

# range(开始，结束，步长) 顾头不顾尾
for i in range(0, 2, 1):
    print(i)
for i in range(10):  # 按0-9遍历
    print(i, end=',')
    print('\n')

# enumerate 返回元组
for i in enumerate(l1):
    print(i)
for i in enumerate(l1, start=1):
    print(i)

# 类型转换
print(tuple(l1))
print(l1)
print(list(t1))
print(set(l1))  # 转成集合会自动去重

# 推导式(生成式) 适用于:列表 集合 字典， 用于简化代码（不需要使用循环即可实现功能）
# 列表推导式：创建或控制有规律的列表
list1 = [i for i in range(10)]
print(list1)
list2 = [i for i in range(10) if i % 2 == 0]
print(list2)
list3 = [(i, j) for i in range(2) for j in range(3)]  # 列表推导式中for循环嵌套
print(list3)

# 字典推导式
dict1 = {i: i ** 2 for i in range(10)}
print(dict1)
d2 = {list1[i]: list2[i] for i in range(4)}
print(d2)
dict3 = {'a': 2, 'b': 2, 'c': 6, 'd': 5, 'e': 7}
d3 = {k: v for k, v in dict3.items() if v >= 5}  # 提取value>=5的键值对
print(d3)

# 集合推导式同上


