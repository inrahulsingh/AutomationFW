class demo():
    x=10
    y=20
    def m1(self):
        print("inside m1 of demo")

class test():
    a=30
    b=40
    def m2(self):
        print("inside m2 of test")

class sample(test,demo):
    p=50
    q=60
    def m3(self):
        print("inside m3 of sample")

print("Properties of demo and test using sample object")
s=sample()
print("x =",s.x)
print("y =",s.y)
s.m1()
print("a =",s.a)
print("b =",s.b)
s.m2()
print("p =",s.p)
print("q =",s.q)
s.m3()
