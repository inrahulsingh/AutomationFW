def add():
    num1=int(input("Enter the first number:\n"))
    num2=int(input("Enter the Second number:\n"))
    res=num1+num2
    print("The sum of",num1,"and",num2,"is",res)

def sub():
    num1=int(input("Enter the first number:\n"))
    num2=int(input("Enter the Second number to substract from first number:\n"))
    res=num1-num2
    print(num1,"minus",num2,"is",res)

def mul():
    num1=int(input("Enter the first number:\n"))
    num2=int(input("Enter the Second number:\n"))
    res=num1*num2
    print(num1,"multiplied by",num2,"is",res)

def div():
    num1=int(input("Enter the dividend\n"))
    num2=int(input("Enter the divisor\n"))
    res=num1/num2
    print(num1,"divided by",num2,"is",res)

def calc():
    num=int(input("Enter your choice:\n1:Addition\n2:Subsctraction\n3:Multiplication\n4:Division\n"))
    if num==1:
        add()
    elif num==2:
        sub()
    elif num==3:
        mul()
    elif num==4:
        div()
    else:
        print("Wrong option selected")
