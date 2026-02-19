balance = 1000  
print("----- ATM MACHINE -----")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    print("Your current balance is:", balance)
elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Amount deposited successfully.")
    print("Updated balance is:", balance)
elif choice == 3:
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance = balance - amount
        print("Remaining balance is:", balance)
        
else:
    print("Invalid choice!")
