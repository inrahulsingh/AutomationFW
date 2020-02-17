num1=int(input("Enter the first number:\n"))
num2=int(input("Enter the second number:\n"))
num3=int(input("Enter the third number:\n"))
num4=int(input("Enter the fourth number:\n"))
if num1>num2:
    if num1>num3:
        if num1>num4:
            print ("%d is largest among the four numbers %d, %d, %d and %d"%(num1,num1,num2,num3,num4))
        elif num4>num2:
            if num4>num3:
                print("%d is largest among the four numbers %d, %d, %d and %d"%(num4,num1,num2,num3,num4))
            else:
                print("%d is largest among the four numbers %d, %d, %d and %d"%(num3,num1,num2,num3,num4))
        else:
            print("%d is largest among the four numbers %d, %d, %d and %d"%(num2,num1,num2,num3,num4))
    elif num3>num2:
        if num3>num4:
            print("%d is largest among the four numbers %d, %d, %d and %d"%(num3,num1,num2,num3,num4))
        else:
            print("%d is largest among the four numbers %d, %d, %d and %d"%(num4,num1,num2,num3,num4))
    else:
        print("%d is largest among the four numbers %d, %d, %d and %d"%(num2,num1,num2,num3,num4))
elif num2>num3:
        if num2>num4:
            print("%d is largest among the four numbers %d, %d, %d and %d"%(num2,num1,num2,num3,num4))
        else:
            print("%d is largest among the four numbers %d, %d, %d and %d"%(num4,num1,num2,num3,num4))
elif num3>num4:
   print("%d is largest among the four numbers %d, %d, %d and %d"%(num3,num1,num2,num3,num4))
else:
   print("%d is largest among the four numbers %d, %d, %d and %d"%(num4,num1,num2,num3,num4))
