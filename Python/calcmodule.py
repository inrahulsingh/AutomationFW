def calc():
    num=int(input("Enter your choice:\n1:Addition\n2:Subsctraction\n3:Multiplication\n4:Division\n"))
    if num==1:
        import addmodule
        addmodule.add()
    elif num==2:
        import submodule
        submodule.sub()
    elif num==3:
        import multmodule
        multmodule.mul()
    elif num==4:
        import divmodule
        divmodule.div()
    else:
        print("Wrong option selected")
