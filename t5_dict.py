dict1 = {'name': 'a', 'age': 2, 'gender': 'male'}

# 创建空字典两种方法
dict2 = {}
dict3 = dict()
print(f'{dict2}\t{dict3}')

# 增
dict2['n'] = 'Tom'
print(dict2)

# 删
del (dict3)  # 删除字典
del dict2['n']  # 删键值对
print(dict2)
# dict1.clear()  # 清空字典

# 查
print(dict1['name'])

print(dict1.get('name', 111))
print(dict1.get('names', 111))  # 不存在返回111
print(dict1.get('names'))  # 不存在默认返回None

print(dict1.keys())
print(dict1.values())
print(dict1.items())  # 返回所有键值对，形式为元组

# 循环遍历
for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

for i in dict1.items():
    print(i)

for key, value in dict1.items():  # 因为返回的元组有两个数据，所以可以拆包
    print(f'{key}的值为{value}')
