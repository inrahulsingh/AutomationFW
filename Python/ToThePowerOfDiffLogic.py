base=int(input("Enter a number:\n"))
power=int(input("Enter to the power value:\n"))
res=1
i=1
while (i<=power):
    res*=base
    i+=1
    print(res)
#res*=base means res=res*base
