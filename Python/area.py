def circle():
    r=int(input("Enter the value of radius:\n"))
    ac=3.14*r*r
    print("Area of circle is",ac)

def triangle():
    h=int(input("Enter the value of height:\n"))
    b=int(input("Enter the value of base:\n"))
    at=h*b*0.5
    print("Area of circle is",at)

def rectangle():
    w=int(input("Enter the value of width:\n"))
    l=int(input("Enter the value of length:\n"))
    ar=w*l
    print("Area of circle is",ar)

def square():
    a=int(input("Enter the value of side:\n"))
    areas=a*a
    print("Area of square is",areas)

def area():
    num=int(input("Enter your choice to calculate area:\n1:Circle\n2:Triangle\n3:Rectangle\n4:Square\n"))
    if num==1:
        circle()
    elif num==2:
        triangle()
    elif num==3:
        rectangle()
    elif num==4:
        square()
    else:
        print("Wrong option selected")
