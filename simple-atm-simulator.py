account_balance = 10000
minimum_balance = 500

while True:
    try:
        #display
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        #taking choice
        user_choice = int(input("enter choice: "))

        #check balance
        if user_choice==1:
            print(f"current balance: ₹{account_balance}")

        #deposit money
        elif user_choice==2:
            deposit_amount = float(input("Enter amount to deposit: "))

            if deposit_amount<=0:
                print("enter amount more than 0")
            else:
                account_balance+=deposit_amount
                print("deposit successful!")
                print(f"New balance: ₹{account_balance}")

        #withdraw money
        elif user_choice==3:
            withdrawal_amount = float(input("enter amount to withdraw: "))

            if withdrawal_amount<=0:
                print("withdrawal amount must be greater than zero")

            elif account_balance-withdrawal_amount<minimum_balance:
                print("withdrawal denied!")
                print(f"minimum balance of ₹{minimum_balance} must be maintained")

            else:
                account_balance -= withdrawal_amount
                print("withdrawal successful!")
                print(f"new balance: ₹{account_balance}")

        #exit
        elif user_choice == 4:
            print("thank you for using the ATM")
            break

        else:
            print("invalid choice")

#exception handling
    except ValueError as ve:
        print("Error: ",ve)

    except Exception as e:
        print("Error: ", e)