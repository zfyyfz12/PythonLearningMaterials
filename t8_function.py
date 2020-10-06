def funName(a, b):
    """这是说明文档"""  # 定义函数说明文档：在第一行用多行注释
    return a + b  # return退出当前函数，return后面代码不执行
    print('haha')


help(funName)  # 查看函数说明文档
print(funName(1, 2))

# 修改全局变量
a = 100


def modify():
    global a  # 声明a为全局变量
    a = 200


modify()
print(a)


# 一个函数多个返回值
def fun1():
    return 1, 2  # 返回的是元组
    # return (1,2)
    # return [1,2]
    # return {'a':1,'b':2}


print(fun1())
num1, num2 = fun1()  # 拆包
print(num1)
print(num2)


# 默认参数（缺省参数）
def user(name, age, gender='male'):
    print(f'姓名:{name}\t年龄:{age}\t性别:{gender}')


user('a', 1)
user('a', 1, 'female')


# 不定长参数(参数个数不确定)
# 1、包裹位置传递
def fun2(*args):  # 返回元组
    print(args)


fun2()
fun2('a')
fun2('a', 1)


# 2、包裹关键字传递
def fun2(**kwargs):  # 返回字典
    print(kwargs)


fun2()
fun2(name='tom')
fun2(name='tom', age=1)
