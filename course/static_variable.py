class Test:
    a = 10

    def __init__(self):
        self.b = 20

    @classmethod
    def m1(cls):
        cls.a = 720
        cls.b = 721


t1 = Test()
t2 = Test()
print("T1:", t1.a, t2.b)
print("T2:", t2.a, t2.b)
Test.a = 888
Test.b = 999  # New static variable will be created, won't use the self.b, (It is similar to class method)
print("T1:", t1.a, t1.b)
print("T2:", t2.a, t2.b)
print("Test:", Test.a, Test.b)
t1.b = 999 # Modifying the instance variable in the class
print("T1:", t1.a, t1.b)

# M1
t1.m1()
print("T1", t1.a, t1.b)
print("T2", t2.a, t2.b)
print("Test", Test.a, Test.b)