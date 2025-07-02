Pin=4567
balance=5000
while True:
    print("ATM menu")
    print("1.check balance")
    print("2.Deposit")
    print("3.withdraw")
    print("4.exit")
    choice=input("enter your choice from 1-4:")
    if choice=="1":
        print("your balance is:balance")
    elif choice=="2":
        amount=input("enter deposit amount:")
        if amount>0:
            balance=balance+amount
            print("amount deposited")
        else:
            print("invalid amount")
    elif choice=="3":
        amount=input("enter amount to withdraw:")
        if 0<amount<=balance:
            balance=balance-amount
            print("amount withdrawn")
        else:
            print("insufficient balance")
