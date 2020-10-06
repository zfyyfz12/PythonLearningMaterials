# 元组属于不可变类型，元组内数据不能修改，只支持查找操作
t1 = (1, 2, 3)
t2 = (100,)  # 定义单个数据元组后面需要加逗号

print(t1[0])
print(t1.index(1))  # 找不到报错
print(t1.count(1))
print(len(t1))

t3 = (1, 2, [3, 4])  # tuple中嵌套的list可以修改
t3[2][0] = 5
print(t3)
