# 1.self表示一個具體的實例本身。如果用了staticmethod，那麼就可以無視這個self，將這個方法當成一個普通的函數使用。
# 2.cls表示這個類本身。
class A(object):
    def foo1(self):
        print("Hello", self)
    @staticmethod
    def foo2():
        print("hello")
    @classmethod
    def foo3(cls):
        print("hello", cls)

a = A()

# 最常見的調用方式，但與下面的方式相同
print(a.foo1())

# 傳入實例a，相當於普通方法的self
print(A.foo1(a))

# 由於靜態方法沒有參數，故可以不傳東西
print(A.foo2())

# 由於是類方法，因此，它的第一個參數為類本身
print(A.foo3())

# 直接輸入A，與上面那種調用返回同樣的信息
print(A)

# 所以由以上測試結果可以得知，類先調用__new__方法，返回該類的實例對象
# 這個實例對象就是__init__方法的第一個參數self，即self是__new__的返回值