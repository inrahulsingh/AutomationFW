class demo:
    def m1(self):
        print("entering m1()")
        x=int(input("Enter the dividend:\n"))
        y=int(input("Enter the divisor:\n"))
        try:
            print("Entering try block")
            print("x/y :",(x/y))
            print("Exiting try block")
        except Exception as z: #except ZeroDivisionError as z:
            print("Exception handeled")
            print(z)
        else:
            print("Entering else block")
        print("Exiting m1()")
d=demo()
d.m1()
