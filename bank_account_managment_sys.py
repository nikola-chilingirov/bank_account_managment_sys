# Enhanced Bank Account Management System with Loan Feature

# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():
    """Create a new bank account."""
    # 1. Prompt the user for the account holder's name.
    name = input('Enter your name: ')
    # 2. Add the new account holder to the list of account holders.
    account_holders.append(name)
    # 3. Initialize the balance to 0 for the new account.
    balances.append(0.0)
    # 4. Initialize an empty transaction history for the new account.
    transaction_histories.append([])
    # 5. Initialize the outstanding loan amount to 0.
    loans.append(0)
    # 6. Notify the user of the successful account creation.
    print('You account is successfully created.')


def deposit():
    """Deposit money into an account."""
    # 1. Prompt the user for the account holder's name.
    acc_holder = input('Please, enter account holder name: ')
    # 2. Check if the account exists in the system.
    if acc_holder in account_holders:
        index_d = account_holders.index(acc_holder)
    # 3. If the account exists, prompt the user for the amount to deposit.
        amount_deposit = float(input('Please, enter the amount to deposit: '))
    # 4. Update the account's balance with the deposited amount.
        #sub_balance = balances[index_d]
        balances[index_d] += amount_deposit
    # 5. Log the transaction in the account's transaction history.
        sub_transaction_histories = transaction_histories[index_d]
        sub_transaction_histories.append(f'deposit {amount_deposit:.2f} lv.')
    # 6. Display the updated balance to the user.
        print(f'Your balance - {balances[index_d]:.2f}')
    # 7. If the account does not exist, inform the user.
    else:
        print("Account not found.")


def withdraw():
    """Withdraw money from an account."""
    # 1. Prompt the user for the account holder's name.
    acc_holder = input('Please, enter account holder name: ')
    # 2. Check if the account exists in the system.
    if acc_holder in account_holders:
        index_w = account_holders.index(acc_holder)
    # 3. If the account exists, prompt the user for the amount to withdraw.
        amount_withdraw = float(input('Please, enter the amount to withdraw: '))
    # 4. Check if there are sufficient funds for the withdrawal.
        if amount_withdraw <= balances[index_w]:
    # 5. If funds are sufficient, update the balance and log the transaction.
            balances[index_w] -= amount_withdraw
    # 6. Display the updated balance to the user.
            print(f'{balances[index_w]:.2f}')
    # 7. If insufficient funds, inform the user.
        else:
            print('Not enough money.')
    # 8. If the account does not exist, inform the user.
    else:
        print("Account not found.")


def check_balance():
    """Check the balance of an account."""
    # 1. Prompt the user for the account holder's name.
    acc_holder = input('Please, enter account holder name: ')
    # 2. Check if the account exists in the system.
    if acc_holder in account_holders:
        index_check = account_holders.index(acc_holder)
    # 3. If the account exists, display the current balance.
        print(f"The balance of account is {balances[index_check]:.2f}")
    # 4. If the account does not exist, inform the user.
    else:
        print("Account not found.")

def list_accounts():
    """List all accounts and their balances."""
    # 1. Check if there are any accounts in the system.
    if len(account_holders) != 0:
    # 2. If there are accounts, loop through each account holder.
        for i in range(len(account_holders)):
            print(f'Name - {account_holders[i]}')
            print(f'Balance - {balances[i]:.2f}')
            print(f'Outstanding loan amount - {loans[i]:.2f}')
            print('--------------')
    # 3. Display the account holder's name, balance, and outstanding loan amount.
    # 4. If there are no accounts, inform the user.
    else:
        print('There are no accounts yet.')

def transfer_funds():
    """Transfer funds between two accounts."""
    # 1. Prompt the user for the sender's and recipient's account holder names.
    sender = input("Please, enter sender's account: ")
    recipient = input("Please, enter recipient's account: ")
    # 2. Check if both accounts exist in the system.
    if sender in account_holders and recipient in account_holders and sender != account_holders:
        index_send = account_holders.index(sender)
        index_recipient = account_holders.index(recipient)
    # 3. If both accounts exist, prompt the user for the amount to transfer.
        amount_transfer = float(input('Please, enter the amount to transfer: '))
    # 4. Check if the sender has sufficient funds for the transfer.
        if amount_transfer <= balances[index_send]:
    # 5. If funds are sufficient, update both balances and log the transactions.
            balances[index_send] -= amount_transfer
            balances[index_recipient] += amount_transfer
            sub_transaction_histories_send = transaction_histories[index_send]
            sub_transaction_histories_send.append(f'send {amount_transfer:.2f} lv. to {recipient}')
            sub_transaction_histories_recipient = transaction_histories[index_recipient]
            sub_transaction_histories_recipient.append(f'receive {amount_transfer:.2f} lv. from {sender}')
    # 6. Inform the user of the successful transfer.
            print('The transfer was successful.')
    # 7. If insufficient funds or if either account does not exist, inform the user.
        else:
            print("The amount in your account is not enough.")
    elif sender in account_holders and recipient not in account_holders:
        print(f"{recipient} have no account.")
    elif sender not in account_holders and recipient in account_holders:
        print(f"{sender} have no account.")
    elif sender not in account_holders and recipient not in account_holders:
        print(f"{sender} and {recipient} have no accounts.")


def view_transaction_history():
    """View transaction history for a specific account."""
    # 1. Prompt the user for the account holder's name.
    acc_holder = input('Please, enter account holder name: ')
    # 2. Check if the account exists in the system.
    if acc_holder in account_holders:
        index_history = account_holders.index(acc_holder)
    # 3. If the account exists, display the transaction history.
        if len(transaction_histories[index_history]) > 0:
            print(f"{transaction_histories[index_history]}")
    # 4. If there are no transactions, inform the user.
        else:
            print(f"This account have no transactions.")
    # 5. If the account does not exist, inform the user.
    else:
        print("Account not found.")


def apply_for_loan():
    """Apply for a loan."""
    acc_holder = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if acc_holder in account_holders:
        index_loan = account_holders.index(acc_holder)  # Find the account index

        # Prompt user for the loan amount they wish to apply for
        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        # Check if the loan amount is within the limit
        if loan_amount <= MAX_LOAN_AMOUNT:
            # Update balance and loan amount
            balances[index_loan] += loan_amount
            loans[index_loan] += loan_amount * (1 + INTEREST_RATE)  # Calculate total loan with interest

            print(f"Loan of {loan_amount:.2f} leva approved for {acc_holder}. New balance: {balances[index_loan]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""
    acc_holder = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if acc_holder in account_holders:
        index_rep = account_holders.index(acc_holder)  # Find the account index

        # Prompt user for repayment amount
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index_rep]:.2f} leva): "))

        # Check if the repayment amount is valid
        if repayment_amount <= loans[index_rep]:
            # Update balance and outstanding loan amount
            balances[index_rep] -= repayment_amount
            loans[index_rep] -= repayment_amount

            print(f"Repayment of {repayment_amount:.2f} leva accepted for {acc_holder}. Remaining loan: {loans[index_rep]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")


main()


