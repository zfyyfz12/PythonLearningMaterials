# 集合数据不允许重复
set1 = {1, 2, 3, 4, 5}
set2 = set('123456')

set3 = set()  # 创建空集合
print(f'{set1}\n{set2}\n{set3}')

set1.add(100)  # 追加单个数据
print(set1)
set1.update([6, 7, 8, 9])  # 追加一个序列的数据
print(set1)

set1.remove(1)  # 若数据不存在报错
set1.discard(1)  # 若数据不存在不报错
print(set1.pop())  # 从左删除并返回
print(set1)

print(1 in set1)
print(10 not in set1)
