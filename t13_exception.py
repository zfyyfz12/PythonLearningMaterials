try:
    open('1.txt', 'r')
except:
    print('1.txt不存在')

try:
    print(num)
except NameError:  # 只捕获该类型的异常
    print('若发生NameError异常，执行此代码')

try:
    print(1 / 0)
except (NameError, ZeroDivisionError):  # 捕获多种类型类型
    print('捕获多种类型类型')

try:
    print(1 / 0)
except (NameError, ZeroDivisionError) as e:  # 捕获异常描述信息，e是变量
    print(e)

try:
    f = open('2.txt', 'r')
except Exception as e:  # Exception是所有异常类的父类
    print(e)

try:
    f = open('1.txt', 'r')
except Exception:
    f = open('1.txt', 'w')
else:  # 没有异常时执行的代码
    print('没异常')
finally:  # 无论有无异常都会执行
    f.close()


# try except可以嵌套

# 自定义异常
class passwordLengthError(Exception):  # 自定义异常类继承自Exception
    def __init__(self, l):
        self.length = l

    def __str__(self):  # 设置异常描述信息
        return f'密码不能少于{self.length}位'


try:
    pw = input('请输入密码')
    if len(pw) < 8:
        raise passwordLengthError(8)  # 抛异常
except Exception as e:
    print(e)
else:
    print('输入密码成功')

