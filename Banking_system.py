
balance = 0
is_running = True


def show_balance():
    global balance
    print(f"your balance is \u20B9{balance:.2f}")

def withdraw():
    global balance
    amount = float(input("Enter your withdraw amount:"))

    if amount > balance:
        print("insufficent balance!")
    elif amount <= 0:
        print("amount must be greater than zero")
    else:
        balance-=amount
        print(f"withdraw amount \u20B9{amount:.2f}")

def deposit():
    global balance
    amount = float(input("Enter your deposite amount:"))

    if amount <= 0:
        print("Thats not a valid amount")
    else:
        balance+=amount
        print(f"Deposited amount \u20B9{amount:.2f}")

def Exit():
    is_running = False


while is_running:
    print("1.Deposite")
    print("2.show Balance")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter a choice (1-4):")

    if choice == "1":
        deposit()
    elif choice == "2":
        show_balance()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        exit()
    else:
        print("invalid choice!")

