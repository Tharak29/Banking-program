def show_balance(balance):
    print(f" your balance is ${balance:.2f}")

def deposit():
    amount = float(input("enter the amount to br deposited : "))

    if amount < 0:
        print("enter a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter amount to be withdrawed : "))

    if amount > balance:
        print(" Insufficiennt balance")

    elif amount < 0:
        print("Amount must be greater than 0")

    else:
        print("successfully withdrawned")
        return amount    

def main():
    balance = 0
    is_running = True
    
    
    while is_running:
        print("Banking program")
        print("1. Show balalance")
        print("2. Deposite")
        print("3. Withdraw ")
        print("4.Exit")
        
        
        choice = input("enter the choice from 1-4: ")
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else :
            print("That is not a valid choice") 
              
   
    print("Thankyou for banking with us")

if __name__ == '__main__':
        main()