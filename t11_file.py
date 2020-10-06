# 打开文件 open(name,mode) 返回文件对象
# r读(若mode省略，默认为r)、w写（会覆盖原有内容）、a追加、
# rb,r+,rb+,wb,w+（会覆盖，所以读取时没有数据）,wb+,a+(a+文件指针在末尾无法读取数据) (后面带+ ： 读写)
f = open('fileOperationTest.txt', 'r')
print(f.read(3))  # 2为读的字节数（包括换行符等），不写参数，=默认读取全部数据
print(f.readlines())  # 返回列表，文件每一行为一个元素
print(f.readline())  # 一次读一行
f1 = open('fileOperationTest.txt', 'w')
f1.write('aaaaa\naaaaa\naaaaa')
f1.close()

# seek（偏移量，起始位置） 用于移动文件指针 （起始位置：0：文件开头 1：当前位置 2：文件结尾）
f2 = open('fileOperationTest.txt', 'r')
f2.seek(3, 0)
print(f2.read())

# 文件和文件夹操作
import os

# os.rename(文件路径,新文件名)
# os.remove(文件路径)
os.mkdir('11112')  # 创建文件夹
os.rmdir('11112')  # 删除文件夹
p = os.getcwd()  # 获取当前文件路径
print(p)

print(os.listdir())  # listdir获取某个文件夹下所有文件，返回列表

# chdir
os.mkdir('aaaaa')  # 创建aaaaa文件夹
os.chdir('aaaaa')  # 改变目录路径到aaaaa文件夹
os.mkdir('bb')  # 在aaaaa文件夹中创建bb文件夹
