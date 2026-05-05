#tables
from SingleEmailSend import SingleEmailSender

accounts = {
    1234:'1234',
    1235:'1235'
}

users = {
    1234: {'username': 'Charan', 'email': 'pcharan87746@gmail.com', 'balance': 1000},
    1235: {'username': 'Sanyu', 'email': '2211cs010518@mallareddyuniversity.ac.in', 'balance':5000}
}


# login

def login(account_no:int, password:str)->bool:
    if account_no in accounts:
        if accounts[account_no] == password:
            return True
        else:
            return False
    else:
        return False


def register(username:str, email:str, password:str, balance:int)->bool:
    print("Register page")
    pass


def get_balance(account_no:int)->int:
    if account_no in users:
        return users[account_no]['balance']
    else:
        return "Account not exists in users table"


# WITHDRAW 
def withdraw(account_no:int, withdraw_amount:int)->str:
    if account_no in users:

        curr_amount = users[account_no]['balance']

        if curr_amount >= withdraw_amount:

            users[account_no]['balance'] -= withdraw_amount

            username = users[account_no]['username']
            receiver = users[account_no]['email']

            subject = "Withdraw Alert"
            body = f"""
Dear {username},

₹{withdraw_amount} withdraw successful.
Current balance: ₹{users[account_no]['balance']}

 
Thank You,
Small Scale Bank
"""

            # EMAIL SENT ONLY AFTER SUCCESS
            SingleEmailSender(receiver, subject, body)

            return f"{withdraw_amount} withdraw successful and current balance is {users[account_no]['balance']}"

        else:
            return "Insufficient Balance"

    else:
        return "Account not exists in database"


# DEPOSIT 
def deposite(account_no:int, deposite_amount:int)->str:
    if account_no in users:

        users[account_no]['balance'] += deposite_amount

        username = users[account_no]['username']
        receiver = users[account_no]['email']

        subject = "Deposit Alert"
        body = f"""
Dear {username},

₹{deposite_amount} deposited successfully.
Current balance: ₹{users[account_no]['balance']}

Thank You,
Small Scale Bank
"""

        # EMAIL SENT ONLY AFTER SUCCESS
        SingleEmailSender(receiver, subject, body)

        return f"{deposite_amount} deposited successfully and current balance is {users[account_no]['balance']}"

    else:
        return "Account not exists in database"


def transfer(from_account:int, to_account:int, transfer_amount:int)->str:

    # check sender account
    if from_account not in users:
        return "Sender account not exists"

    # check receiver account
    if to_account not in users:
        return "Receiver account not exists"

    sender_balance = users[from_account]['balance']

    # check sufficient balance
    if sender_balance < transfer_amount:
        return "Insufficient Balance"

    # deduct from sender
    users[from_account]['balance'] -= transfer_amount

    # add to receiver
    users[to_account]['balance'] += transfer_amount

    # ---------- SENDER EMAIL ----------
    sender_name = users[from_account]['username']
    sender_email = users[from_account]['email']

    subject = "Amount Transfer Debit Alert"

    body = f"""
Dear {sender_name},

₹{transfer_amount} transferred successfully to account {to_account}.

Current Balance: ₹{users[from_account]['balance']}

Thank You,
Small Scale Bank
"""

    SingleEmailSender(sender_email, subject, body)

    # ---------- RECEIVER EMAIL ----------
    receiver_name = users[to_account]['username']
    receiver_email = users[to_account]['email']

    subject = "Amount Credit Alert"

    body = f"""
Dear {receiver_name},

₹{transfer_amount} received from account {from_account}.

Current Balance: ₹{users[to_account]['balance']}

Thank You,
Small Scale Bank
"""

    SingleEmailSender(receiver_email, subject, body)

    return f"₹{transfer_amount} transferred successfully from {from_account} to {to_account}"

def ministatement(account_no:int)->str:
    print("Ministatement page under development process...")
    pass


def logout():
    exit()


# MAIN PROGRAM

if __name__ == "__main__":

    print("Welcome to the small scale bank")
    print("Select your operation: \n 1. Login \n 2. Register")

    choice = int(input("Select your operation:"))

    if choice == 1:

        account = int(input("Enter your account number:"))
        password = input("Enter your Password:")

        login_val = login(account_no=account, password=password)

        while login_val:

            print("\nSelect Your Operation :")
            print("1. Get Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Ministatement")
            print("6. Logout")

            choice = int(input("Select your operation choice:"))

            if choice == 1:
                print("Current Balance:", get_balance(account_no=account))

            elif choice == 2:
                amount = int(input("Enter Withdraw amount: "))
                print(withdraw(account_no=account, withdraw_amount=amount))

            elif choice == 3:
                amount = int(input("Enter Deposit amount: "))
                print(deposite(account_no=account, deposite_amount=amount))

            elif choice == 4:
                transfer(1,1,1)

            elif choice == 5:
                ministatement(1)

            elif choice == 6:
                logout()

            else:
                print("Select valid operation(1-6)")

    elif choice == 2:
        register(1,1,1,1)

    else:
        print("Please select valid operation")