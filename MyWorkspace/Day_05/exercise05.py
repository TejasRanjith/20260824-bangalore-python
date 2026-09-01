AUDIT_TRANSACTION_COUNT = 0

def create_bank_account(owner_name, initial_balance):
    global AUDIT_TRANSACTION_COUNT
    balance = float(initial_balance)
    history = ["Account created with 1000.0"]
    
    def deposit(amount):
        global AUDIT_TRANSACTION_COUNT
        balance += amount
        history.append(f"Deposit of {amount}")
        AUDIT_TRANSACTION_COUNT+=1