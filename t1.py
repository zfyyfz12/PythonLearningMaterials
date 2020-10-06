import random

num1 = [1, 2, 3]
num2 = {1, 2, 3}
num3 = {'1': 1, 'two': 2}
num4 = (1, 2, 3)
age = 1811
name = 't'
weight = 70.0
stu = 1
print(type(num1), end='\t')  # 更改结束符end，end默认\n
print('name=%.2f,\n%06d' % (weight, age))  # 格式化输出·
print(f'{age}\t{type(num2)}\t{type(num3)}\t{type(num4)}')  # f格式化字符串
p = input('请输入')  # input接收到的数据类型都当做是字符串

# 循环
a = random.randint(1, 3)
b = 0
while b <= 3:
    if a == 1:
        print(f'{a}')
    elif a == 2:
        print(f'{a}')
    else:
        break  # break之后不执行else,正常结束才执行else
    b += 1
else:
    print('a==1') if a == 1 else print('a!=1')

# 交换
a, b = 1, 2
a, b = b, a
print(f'{a}\t{b}')

# id()返回变量内存地址，可以用来判断两个变量是否为同一个值的引用
a = 1
b = a
print(id(a))
print(id(b))
a = 2
print(id(a))
print(id(b))
