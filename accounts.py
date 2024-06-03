class Account:
    def __init__(self, number, pin):
        self.number = number
        self.__pin = pin
        self.__balance = 0
    def check_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
    def deposit(self, amount, pin):
        if pin == self.__pin:
            self.__balance += amount
            return f"Deposit successful. New balance: {self.__balance}"
        else:
            return "Wrong pin"
    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if self.__balance >= amount:
                self.__balance -= amount
                return f"Withdrawal successful. New balance: {self.__balance}"
            else:
                return "Insufficient balance"
        else:
            return "Wrong pin"
    def view_account_details(self, pin):
        if pin == self.__pin:
            return f"Account Number: {self.number}\nBalance: {self.__balance}"
        else:
            return "Wrong pin"
    def change_account_owner(self, new_pin, pin):
        if pin == self.__pin:
            self.__pin = new_pin
            return "Account owner changed successfully"
        else:
            return "Wrong pin"
    def account_statement(self, pin):
        if pin == self.__pin:
            return f"Account Statement:\nAccount Number: {self.number}\nBalance: {self.__balance}"
        else:
            return "Wrong pin"
    def set_overdraft_limit(self, limit, pin):
        if pin == self.__pin:
            self.__overdraft_limit = limit
            return "Overdraft limit set successfully"
        else:
            return "Wrong pin"
    def interest_calculation(self, rate, pin):
        if pin == self.__pin:
            self.__balance += self.__balance * rate
            return f"Interest calculated successfully. New balance: {self.__balance}"
        else:
            return "Wrong pin"
    def freeze_account(self, pin):
        if pin == self.__pin:
            self.__frozen = True
            return "Account frozen successfully"
        else:
            return "Wrong pin"
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.__frozen = False
            return "Account unfrozen successfully"
        else:
            return "Wrong pin"
    def transaction_history(self, pin):
        if pin == self.__pin:
            return f"Transaction History:\n[Insert transaction history here]"
        else:
            return "Wrong pin"
    def set_minimum_balance(self, min_balance, pin):
        if pin == self.__pin:
            self.__minimum_balance = min_balance
            return "Minimum balance set successfully"
        else:
            return "Wrong pin"
    def transfer_funds(self, amount, recipient_account, pin):
        if pin == self.__pin:
            if self.__balance >= amount:
                self.__balance -= amount
                recipient_account.deposit(amount, recipient_account.__pin)
                return f"Transfer successful. New balance: {self.__balance}"
            else:
                return "Insufficient balance"
        else:
            return "Wrong pin"
    def close_account(self, pin):
        if pin == self.__pin:
            self.__balance = 0
            self.__pin = None
            return "Account closed successfully"
        else:
            return "Wrong pin"