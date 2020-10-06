# 字符串属于不可变类型，不能改
str1 = 'abcde'
print(str1[0])  # 下标
print(str1[0:4:1])  # 切片 下标范围：顾头不顾尾
print(str1[4:0:-1])
print(f'{str1[:5]}\t{str1[2:]}')
print(str1[-4:-1])  # 下标-1是最后一个数字

print(str1.find('cd'))  # 查找子串是否存在在str1中并返回开始下标，找不到返回-1，
print(str1.rfind('cd'))  # 从右找,但下标还是从左开始计算
print(str1.find('cd', 1, 3))  # 在下标范围内找子串，不包含下标3

print(str1.index('cd'))  # 查找子串下标，找不到报错，
print(str1.rindex('cd'))  # 从右找,但下标还是从左开始计算
print(str1.index('cd', 1, 4))

print(str1.count('cd'))  # 查找子串是出现次数
print(str1.count('cd', 1, 3))

b = 'abce dabce dabc de'
newb = b.replace("a", 'z')  # 默认全部替换
nb = b.replace('a', 'z', 1)  # 1 为替换次数
print(f'{b}\t{newb}\t{nb}')

newb = b.split("a")  # 默认全部分割，返回列表
nb = b.split('a', 2)  # 2 为分割字符数
print(f'{b}\t{newb}\t{nb}')

list1 = ['aa', 'bb', 'cc']
newStr = '...'.join(list1)  # 用...来连接字符串
print(newStr)

newb = b.title()  # 首字母大写
print(newb)

newb = b.capitalize()  # 每个单词首字母大写
print(newb)

newb = b.upper()
nb = newb.lower()
print(f'{newb}\t{nb}')

c = '   abcde   '
nc1 = c.lstrip()  # 删左边空白
nc2 = c.rstrip()
nc3 = c.strip()  # 删两侧空白
print(f'{nc1}\t{nc2}\t{nc3}')

c = 'abcde'
nc1 = c.ljust(10, '.')  # 左对齐，用.填充
nc2 = c.rjust(10, '.')
nc3 = c.center(10, '.')  # 居中对齐，用.填充
print(f'{nc1}\t{nc2}\t{nc3}')

c = 'abcdefghijklmn'
nc1 = c.startswith('ab', 0, 5)  # 判断是否以ab开头
nc2 = c.endswith('ab', 0, 1)  # 判断是否以ab开头
print(f'{nc1}\t{nc2}\t')

c = 'abcdefgh12345'
d = '  '
nc1 = c.isalpha()  # 只含字母返回true
nc2 = c.isdigit()  # 只含字母返回true
nc3 = c.isalnum()  # 只含数字或字母true
nc4 = d.isspace()  # 只含空格返回true
print(f'{nc1}\t{nc2}\t{nc3}\t{nc4}')
