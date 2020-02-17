def atm():
    upin=int(input("Enter the PIN:\n"))
    dbpin=1234
    dbbalance=1000
    if upin==dbpin:
        print("PIN validation successfull!\n")
        uamount=int(input("Enter the amount:\n"))
        if uamount<=dbbalance:
            print("Transaction successfull!\n")
        else:
            print("Transaction failed! Insufficient balance.\n")
    else:
        print("Invalid PIN!\n")
