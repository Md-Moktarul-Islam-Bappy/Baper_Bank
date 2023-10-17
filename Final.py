import random
 
class Bank:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.users = []
        self.total_balance = 0
        self.total_loan = 0
        self.is_bankrupt = False
        self.is_loan_system_enabled = True
 
class AccountHolder:
    def __init__(self, name, email, address, account_type, password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.password = password
        self.balance = 0
        self.account_no = random.randint(500, 5000)
        self.transaction_history = []
        self.loan_count = 0
 
    def set_password(self, password):
        self.password = password
 
    def deposit(self, bank, amount):
        if not bank.is_bankrupt:
            if amount > 0:
                self.bank = bank
                self.balance += amount
                self.bank.total_balance += amount
                history = f"Successfully deposited: ${amount}. New Balance: ${self.balance}"
                self.transaction_history.append(history)
                print(history)
            else:
                print(f"Invalid deposit amount. Please try again!")
        else:
            print("The bank is bankrupt. You cannot deposit money.")
 
    def withdraw(self, bank, amount):
        if not bank.is_bankrupt:
            if 0 < amount <= self.balance:
                self.bank = bank
                self.balance -= amount
                self.bank.total_balance -= amount
                history = f"Withdrawn: ${amount}. New Balance: ${self.balance}"
                self.transaction_history.append(history)
                print(history)
            elif amount > self.balance:
                print("Withdrawal amount exceeds your balance.")
            else:
                print("Invalid amount request. Please try again!")
        else:
            print("The bank is bankrupt. You cannot withdraw money.")
 
    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
 
    def show_transaction_history(self):
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transaction history.")
 
    def request_loan(self, bank, amount):
        self.bank = bank
        if not self.bank.is_bankrupt:
            if self.bank.is_loan_system_enabled:
                if self.loan_count < 2:
                    self.balance += amount
                    self.bank.total_balance -= amount
                    self.bank.total_loan += amount
                    history = f"Loan issued successfully. ${amount} added to your account."
                    self.transaction_history.append(history)
                    self.loan_count += 1
                    print(history)
                else:
                    print("Sorry! You cannot take more than 2 loans.")
            else:
                print("The bank loan system is currently turned off.")
        else:
            print("The bank is bankrupt. You cannot request a loan.")
 
    def transfer_money(self, bank, amount, recipient_name):
        self.bank = bank
        if len(self.bank.users) >= 2:
            for recipient in self.bank.users:
                if recipient_name == recipient.name:
                    if self.balance >= amount:
                        recipient.balance += amount
                        self.balance -= amount
                        history = f"Balance successfully transferred to {recipient_name} from {self.name}. Amount: ${amount}"
                        self.transaction_history.append(history)
                        print(history)
                        return
                    else:
                        print("Transaction amount exceeds your balance.")
                        return
            else:
                print(f"Recipient with the name {recipient_name} does not exist.")
        else:
            print("There are not enough users to make a transfer.")
 
 
class BankAdministrator:
    def __init__(self, bank) -> None:
        self.bank = bank
        self.username = "admin"
        self.password = "000111"
 
    def list_users(self):
        if self.bank.users:
            print(f"List of registered users:")
            for user in self.bank.users:
                print(f"Name: {user.name}, Account No: {user.account_no}, Email: {user.email}, Address: {user.address}, Account Type: {user.account_type}")
                print()
        else:
            print("No users found.")
 
    def check_total_balance(self):
        print(f"Total balance of {self.bank.name} bank is ${self.bank.total_balance}")
 
    def check_total_loan(self):
        print(f"Total loan amount of {self.bank.name} bank is ${self.bank.total_loan}")
 
    def toggle_loan_system(self, status):
        if status == "1":
            self.bank.is_loan_system_enabled = True
            print("The loan system is now turned on!")
        elif status == "2":
            self.bank.is_loan_system_enabled = False
            print("The loan system is now turned off!")
        else:
            print("Invalid status selection. Please try again!")
 
    def toggle_bankruptcy_status(self, status):
        if status == "1":
            self.bank.is_bankrupt = True
            print(f"{self.bank.name} bank has been declared bankrupt by the administrator.")
        elif status == "2":
            self.bank.is_bankrupt = False
            print(f"{self.bank.name} bank is no longer bankrupt. It has been reopened by the administrator!")
        else:
            print("Invalid status selection. Please try again!")
 
    def delete_user(self, email):
        for user in self.bank.users:
            if user.email == email:
                self.bank.users.remove(user)
                print(f"User {user.name} has been deleted successfully.")
                return
        print("User not found!")
 
 
class UserAuthentication:
    def __init__(self) -> None:
        self.logged_in_user = None
 
    def register_user(self, bank, user):
        for existing_user in bank.users:
            if user.email == existing_user.email:
                print("User already registered!")
                return
        bank.users.append(user)
        print(f"User {user.name} has been registered successfully!")
 
    def login(self, bank, email, password):
        for user in bank.users:
            if user.email == email and user.password == password:
                self.logged_in_user = user
                print(f"Welcome, {user.name}! You have successfully logged in.")
                return True
        print("Invalid email or password. Please try again!")
 
    def log_out(self):
        self.logged_in_user = None
 
 
baper_bank = Bank("Baper Bank", "Dhaka")
admin_user = BankAdministrator(baper_bank)
user_authenticator = UserAuthentication()
 
while True:
    print(f"Welcome to {baper_bank.name}")
    print("Log in as Admin: Username - admin, Password - 000111")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    choice = input("Enter your choice:")
 
    if choice == "1":
        print("Admin Login")
        username = input("Enter admin username:")
        password = input("Enter admin password:")
        if username == admin_user.username and password == admin_user.password:
            print("Admin successfully logged in.")
            while True:
                print("1. Create user account")
                print("2. List all user accounts")
                print("3. Check total available balance")
                print("4. Check total loan amount")
                print("5. Delete user account")
                print("6. Toggle loan system")
                print("7. Toggle bankruptcy status")
                print("8. Log Out")
                option = input("Enter your choice:")
 
                if option == "1":
                    name = input("Enter user name:")
                    email = input("Enter user email:")
                    address = input("Enter user address:")
                    account_type = input("Enter '1' for 'Savings' or '2' for 'Current' account:")
                    password = input("Enter user password:")
                    if account_type == "1":
                        new_user = AccountHolder(name, email, address, "Savings", password)
                    elif account_type == "2":
                        new_user = AccountHolder(name, email, address, "Current", password)
                    else:
                        print("Invalid account type. Please try again!")
                        continue
                    user_authenticator.register_user(baper_bank, new_user)
                elif option == "2":
                    admin_user.list_users()
                elif option == "3":
                    admin_user.check_total_balance()
                elif option == "4":
                    admin_user.check_total_loan()
                elif option == "5":
                    email = input("Enter user email:")
                    admin_user.delete_user(email)
                elif option == "6":
                    status = input("Enter '1' to enable or '2' to disable the loan system:")
                    admin_user.toggle_loan_system(status)
                elif option == "7":
                    status = input("Enter '1' to declare bankruptcy or '2' to reopen the bank:")
                    admin_user.toggle_bankruptcy_status(status)
                elif option == "8":
                    break
                else:
                    print("Invalid selection. Please try again!")
 
        else:
            print("Invalid username or password. Please try again!")
 
    elif choice == "2":
        if baper_bank.users:
            print("User Login")
            user_email = input("Enter user email:")
            password = input("Enter password:")
            logged_in = user_authenticator.login(baper_bank, user_email, password)
            if logged_in:
                while True:
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Transfer Money")
                    print("5. Transaction History")
                    print("6. Request Loan")
                    print("7. Log Out")
                    option = input("Enter your choice:")
                    user = user_authenticator.logged_in_user
 
                    if option == "1":
                        user.check_balance()
                    elif option == "2":
                        amount = int(input("Enter amount to deposit: $"))
                        user.deposit(baper_bank, amount)
                    elif option == "3":
                        amount = int(input("Enter amount to withdraw: $"))
                        user.withdraw(baper_bank, amount)
                    elif option == "4":
                        recipient_name = input("Enter recipient's name:")
                        amount = int(input("Enter amount to transfer: $"))
                        user.transfer_money(baper_bank, amount, recipient_name)
                    elif option == "5":
                        user.show_transaction_history()
                    elif option == "6":
                        loan_amount = int(input("Enter loan amount: $"))
                        user.request_loan(baper_bank, loan_amount)
                    elif option == "7":
                        user_authenticator.log_out()
                        break
                    else:
                        print("Invalid choice. Please try again!")
 
            else:
                print("No user found. Please try again!")
 
        else:
            print("No users registered. Please contact the admin.")
 
    elif choice == "3":
        print("Thank you for using our banking system. Goodbye!")
        break
 
    else:
        print("Invalid choice. Please try again!")
