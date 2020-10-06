__all__ = ['A']  # 如果有__all__列表，则用from t14_module import *时，只能导入all列表中的方法


def A(a, b):
    print(a + b)


def B(a, b):
    print(a * b)


# 测试模块中方法
if __name__ == '__main__':
    A(1, 2)
    B(1, 2)
