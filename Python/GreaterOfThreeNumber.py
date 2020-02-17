num1=int(input("Enter first number:\n"))
num2=int(input("Enter second number:\n"))
num3=int(input("Enter third number:\n"))
if num1>num2:
    if num1>num3:
        print('%d is greater than %d and %d'%(num1,num2,num3))
    else:
        print('%d is greater than %d and %d'%(num3,num1,num2))
elif num2>num3:
    print ('%d is greater than %d and %d'%(num2,num1,num3))
else:
    print('%d is greater than %d and %d'%(num3,num1,num2))
