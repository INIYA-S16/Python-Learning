Balance=5000
while True:
    print("1.Deposit Money")
    print("2.Withdrawl Money")
    print("3.Show Account Detail")
    print("4.Check Account Status")
    print("5.Exit")
    choice=int(input("Enter the Choice:"))
    match choice:
        case 1:
            Deposit=int(input("Enter the Deposit money:"))
            if Deposit >0:
                Balance=Balance+Deposit
                print("Deposit Amount:",Deposit)
                print("Available Balance:",Balance)
            else:
                print("Invalid Amount")
        case 2:
            print("Currrent Balance:",Balance)
            withdrawl=int(input("Enter the Withdrawl Amount:"))
            if withdrawl <=0 :
                print("Invalid Input ")
            elif withdrawl <= Balance:
                if (Balance - withdrawl >= 1000):
                    print("Yes Withdrawl Money")
                    Balance=Balance-withdrawl
                    print("Current Balance:",Balance)
                else:
                    print("Sorry Minimum Balance should be maintained")
            else:
                print("Insufficient Amount")
        case 3:
            print("Current Balance:",Balance)
        case 4:
            if Balance >=5000:
                print("Premium Account")
            elif Balance >=2000:
                print("Good Balance")
            elif Balance >= 500:
                print("Low Balance")
            else:
                print("Very Low Balance")
        case 5:
            print("Thanking For Choosing the Smart Banking")
            break
        case _:
            print("Invalid Option")