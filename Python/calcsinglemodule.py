import Calculator as c
def calcm():
    num=int(input("Enter your choice:\n1:Addition\n2:Subsctraction\n3:Multiplication\n4:Division\n"))
    if num==1:
        print("Addition selected")
        c.add()
    elif num==2:
        print("Subsctraction selected")
        c.sub()
    elif num==3:
        print("Multiplication selected")
        c.mul()
    elif num==4:
        print("Division selected")
        c.div()
    else:
        print("Wrong option selected")
