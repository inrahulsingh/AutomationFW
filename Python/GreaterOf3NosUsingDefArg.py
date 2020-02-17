def fun(a=10,b=20,c=30):
    if a>b:
        if a>c:
            print(a,"is greater than",b,"and",c)
        else:
            print(c,"is greater than",a,"and",b)
    elif b>c:
        print(b,"is greater than",a,"and",c)
    else:
        print(c,"is greater than",a,"and",b)
fun(40,10,50)
            
