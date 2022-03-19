# 有時定義類別時可能會需要調用相同類別內的其他方法，此時要調用内部的方法時，方法前面加 self.
class MyClass:
    def __init__(self):
        pass

    def func1(self):
        # do something
        print('a')  # for example
        self.common_func()

    def func2(self):
        # do something
        self.common_func()

    def common_func(self):
        pass

# 抑或是利用@classmethod裝飾器來做直接調用內部初始值或是函數
class A(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls())
        # 直接調用初始值
        print(cls.bar)
        # 直接調用func1函數
        print(cls().func1())

# 不用實例化，直接調用類函數輸出即可
A.func2()