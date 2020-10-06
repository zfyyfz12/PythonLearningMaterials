# 高阶函数，让代码更简单
def sum2(a, b, f):
    return f(a) + f(b)


print(sum2(1, 2, abs))
print(sum2(1, 2, round))  # 四舍五入,再相加


# 内置高阶函数
# map 返回迭代器
def func(x):
    return x ** 2


l1 = [1, 2, 3, 4, 5]
result = map(func, l1)
print(list(result))

# reduce(func,list) func必须有两个参数
import functools


def func2(a, b):
    return a + b


print(functools.reduce(func2, l1))


# filter(func,list) 过滤掉不符合条件的数据，返回filter对象
def func3(a):
    return a % 2 == 0


print(list(filter(func3, l1)))

