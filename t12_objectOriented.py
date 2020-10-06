class Washer:
    def wash(self):  # self指调用该方法的对象
        print('wash')
        print(self)
        print(self.width)  # 在类中打印对象的实例属性


haier = Washer()
print(haier)
haier.width = 400  # 在类外为对象添加实例属性
haier.wash()


# 魔法方法(具有特殊功能的函数)
class Washer2:
    def __init__(self, wid=1000):  # init魔法方法：创建对象时自动调用
        self.width = wid
        self.__height = 10  # 在属性前加__定义为私有属性，不能继承

    def get_height(self):  # 习惯上定义’get_属性名‘函数获取私有属性值
        return self.__height

    def set_height(self):  # 习惯上定义’set_属性名‘函数设置私有属性值
        self.__height = 100

    def __str__(self):  # str魔法方法：返回对象描述信息（打印对象时返回return后的东西,而不是返回内存地址）
        return '哈哈哈哈哈'

    def __del__(self):  # del魔法方法：删除方法时自动调用
        print('对象已删除')

    def print_info(self):
        print(self.width)

    def __haha(self):  # 在方法前加__定义为私有方法，不能继承
        print('haha')


haixin1 = Washer2(500)
haixin2 = Washer2(600)
haixin1.print_info()
haixin2.print_info()
print(haixin1)


# 继承 子类默认继承父类所有属性和方法
class A(Washer2):
    pass  # 空语句，为了保持程序结构的完整性


A().print_info()


# 多继承：一个子类同时继承多个父类
class B(Washer, Washer2):  # 优继承第一个父类的同名属性和方法
    def __init__(self):  # 重写
        self.width = 10000

    def print_info(self):
        self.__init__()  # 若不加，如果先调用父类同名方法，则属性为父类，所以要加
        print(self.width)

    def fu(self):  # 调用父类同名方法
        # 法一
        Washer2.__init__(self)
        Washer2.print_info(self)
        # 法二 super会自动查找父类，顺序为__mro__顺序
        super().__init__()
        super().print_info()


zi1 = B()
zi1.fu()
zi1.print_info()

print(B.__mro__)  # 显示继承关系

# 多态
# 类属性
# 类方法
# 静态方法
