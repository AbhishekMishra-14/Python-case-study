import random

# Dictionary to hold all accounts
accounts = {}
transactions = {}

# Function to display the menu
def display_menu():
    print("\n1. Create Account")
    print("2. View Account Details")
    print("3. Withdraw")
    print("4. Deposit")
    print("5. Fund Transfer")
    print("6. Print Transaction History")
    print("7. Exit")

# Functions for saving and loading data
def save_data_to_file():
    with open("accounts.txt", "w") as acc_file:
        for account_number, details in accounts.items():
            acc_file.write(f"{account_number},{details['name']},{details['balance']}\n")
    
    with open("transactions.txt", "w") as trans_file:
        for account_number, trans_list in transactions.items():
            for trans in trans_list:
                trans_file.write(f"{account_number},{trans}\n")

def load_data_from_file():
    global accounts, transactions
    try:
        with open("accounts.txt", "r") as acc_file:
            for line in acc_file:
                account_number, name, balance = line.strip().split(',')
                accounts[int(account_number)] = {'name': name, 'balance': float(balance)}
        
        with open("transactions.txt", "r") as trans_file:
            for line in trans_file:
                account_number, transaction = line.strip().split(',', 1)
                if int(account_number) not in transactions:
                    transactions[int(account_number)] = []
                transactions[int(account_number)].append(transaction)
    except FileNotFoundError:
        # No data found, so start with empty dictionaries
        accounts = {}
        transactions = {}

# Functions for various operations
def create_account():
    name = input("Enter your name: ")
    initial_balance = float(input("Enter initial deposit: "))
    account_number = random.randint(10000, 99999)
    
    accounts[account_number] = {
        'name': name,
        'balance': initial_balance
    }
    transactions[account_number] = [] # To store transactions for this account
    print(f"Account created successfully! Your account number is: {account_number}")
    
    save_data_to_file() # Save the updated accounts and transactions

def view_account_details():
    account_number = int(input("Enter account number: "))
    
    if account_number in accounts:
        account = accounts[account_number]
        print(f"Account Holder: {account['name']}")
        print(f"Balance: {account['balance']}")
    else:
        print("Account not found!")

def withdraw():
    account_number = int(input("Enter account number: "))
    
    if account_number in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[account_number]['balance']:
            accounts[account_number]['balance'] -= amount
            transactions[account_number].append(f"Withdraw: {amount}")
            print(f"Withdrawal successful! New balance: {accounts[account_number]['balance']}")
            
            save_data_to_file() # Save the updated accounts and transactions
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def deposit():
    account_number = int(input("Enter account number: "))
    
    if account_number in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[account_number]['balance'] += amount
        transactions[account_number].append(f"Deposit: {amount}")
        print(f"Deposit successful! New balance: {accounts[account_number]['balance']}")
        
        save_data_to_file() # Save the updated accounts and transactions
    else:
        print("Account not found!")

def fund_transfer():
    from_account = int(input("Enter your account number: "))
    to_account = int(input("Enter the recipient's account number: "))
    
    if from_account in accounts and to_account in accounts:
        amount = float(input("Enter amount to transfer: "))
        
        if amount <= accounts[from_account]['balance']:
            accounts[from_account]['balance'] -= amount
            accounts[to_account]['balance'] += amount
            
            transactions[from_account].append(f"Transferred {amount} to {to_account}")
            transactions[to_account].append(f"Received {amount} from {from_account}")
            
            print(f"Transfer successful! New balance for {from_account}: {accounts[from_account]['balance']}")
            
            save_data_to_file() # Save the updated accounts and transactions
        else:
            print("Insufficient balance!")
    else:
        print("Invalid account number(s)!")

def print_transaction_history():
    account_number = int(input("Enter account number: "))
   
    if account_number in transactions:
        print(f"Transaction History for Account {account_number}:")
        for transaction in transactions[account_number]:
            print(transaction)
    else:
        print("Account not found or no transactions available!")

# Main loop
def main():
    load_data_from_file()  # Load the data from file at the start

    while True:
        display_menu()
        choice = input("Enter your choice: ")
       
        if choice == '1':
            create_account()
        elif choice == '2':
            view_account_details()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            deposit()
        elif choice == '5':
            fund_transfer()
        elif choice == '6':
            print_transaction_history()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")

# Run the main program
if __name__ == "__main__":
    main()