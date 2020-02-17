def atm(pin):
    if pin==1234:
        print("Valid PIN")
        amount=int(input("Enter the amount"))
        if amount<=1000:
            print("Transaction Successfull")
        else:
            print("Insufficient balance")
    else:
        print("Invalid PIN")
