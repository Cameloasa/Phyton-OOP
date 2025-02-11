from src.country import Country
from src.user import User
from src.bank_account import BankAccount

print("User")
my_user = User("romanian", "Cami", "1234")
print(my_user)
print(my_user.get_password())
print(my_user.password)
my_user.is_correct_login("Cami","1234")

print("************")
print("Countries")
# Skapa objekt för Sverige, Norge, Island och Danmark
se = Country("Sverige", 10.5, 447425)
no = Country("Norge", 5.5, 385207)
island = Country("Island", 0.38, 103000)
danmark = Country("Danmark", 6.0, 42924)
romania = Country("Romania",19.5,None)

# Lägg till språk
se.add_language("Svenska")
no.add_language("Norska")
no.add_language("Svenska")
island.add_language("Isländska")
danmark.add_language("Danska")
romania.add_language("Romanian")

# Testa print_info-metoden
se.print_info()
no.print_info()
island.print_info()
danmark.print_info()
romania.print_info()

account = BankAccount()
print("************")
print(" Welcome to your Bank Account")

is_running = True

while is_running:
    print("*************************")
    print("     Banking program     ")
    print("*************************")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("*************************")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your balance is: {account.show_balance()} kr")
    elif choice == '2':
        amount = float(input("Enter deposit amount: "))
        try:
            account.deposit(amount)  # deposit() med amount
            print(f"Deposited {amount} kr. New balance: {account.show_balance()} kr")
        except ValueError as e:
            print(f"Error: {e}")  # Error amount < 0
    elif choice == '3':
        amount = float(input("Enter withdrawal amount: "))
        try:
            account.withdraw(amount)  # withdraw() med amount
            print(f"Withdrawn {amount} kr. New balance: {account.show_balance()} kr")
        except ValueError as e:
            print(f"Error: {e}")  # Error
    elif choice == '4':
        is_running = False
    else:
        print("*************************")
        print("That is not a valid choice")
        print("*************************")

print("*************************")
print("Thank you! Have a nice day!")
print("*************************")

