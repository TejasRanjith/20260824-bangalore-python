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
    def withdraw(amount):
        global AUDIT_TRANSACTION_COUNT
        if balance>=amount:
            balance-=amount
            history.append(f"Withdrawal of {amount}")
        else:
            raise ValueError("Insufficient Balance")
    
    return {
        "deposit":deposit,
        "withdraw":
    }

acc = create_bank_account('tejas',10)
acc[]

            