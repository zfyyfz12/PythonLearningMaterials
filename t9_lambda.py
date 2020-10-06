# 也叫匿名函数，作用：简化代码，减少内存开销
# 参数可有可无，可接收人和数量参数，但只有一个返回值
# lambda 参数列表：返回值
fun1 = lambda: 100
fun2 = lambda a, b, c: a + b + c
fun3 = lambda a, b, c=100: a + b + c
fun4 = lambda *args: args  # 返回一个元组
fun5 = lambda **kwargs: kwargs  # 返回一个字典
fun6 = lambda a, b: a if a > b else b  # 带判断的lambda
print(fun1())
print(fun2(1, 2, 3))
print(fun3(1, 2))
print(fun3(1, 2, 99))
print(fun4(1, 2, 3))
print(fun5(name='z', age=1))
print(fun6(5, 9))

# 列表数据按key值排序
# 主要是了解sort()函数中参数key的意思：
# 传递给key参数的是一个函数，它指定可迭代对象中的每一个元素来按照该函数进行排序
stu = [
    {'name': 'Tom'},
    {'name': 'Rose'},
    {'name': 'Jace'},
]
stu.sort(key=lambda x: x['name'])
print(stu)

