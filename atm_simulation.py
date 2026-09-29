print("==========================================")
print("             ATM SIMULATION")
print("==========================================")

correct_pin = "1234"
balance = 10000.00
transactions = []

attempts = 3
logged_in = False

while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        logged_in = True
        print("\nLogin successful!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")
        print("Attempts remaining:", attempts)

if not logged_in:
    print("Your account is temporarily locked.")
else:
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nCurrent Balance: ₹", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                transactions.append(f"Deposited: ₹{amount:.2f}")
                print("Deposit successful.")
                print("Updated Balance: ₹", balance)
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                transactions.append(f"Withdrawn: ₹{amount:.2f}")
                print("Please collect your cash.")
                print("Remaining Balance: ₹", balance)

        elif choice == "4":
            print("\n========== MINI STATEMENT ==========")

            if len(transactions) == 0:
                print("No transactions available.")
            else:
                for transaction in transactions:
                    print(transaction)

            print("Current Balance: ₹", balance)

        elif choice == "5":
            old_pin = input("Enter current PIN: ")

            if old_pin == correct_pin:
                new_pin = input("Enter new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    correct_pin = new_pin
                    print("PIN changed successfully.")
                else:
                    print("PIN must contain exactly 4 digits.")
            else:
                print("Incorrect current PIN.")

        elif choice == "6":
            print("\nThank you for using the ATM.")
            print("Please collect your card.")
            break

        else:
            print("Invalid choice. Please try again.")
