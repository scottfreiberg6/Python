class BankAccount:
    all_accounts=[]
    def __init__(self, int_rate = 0.01, account_balance=0):
        self.int_rate= int_rate
        self.account_balance = account_balance
        BankAccount.all_accounts.append(self)
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        if (self.account_balance - amount)>=0:
            self.account_balance -= amount
        else:
            self.account_balance-=5
            print(f"Insufficent fund: Charging $5 fee")
        return self
    def display_account_info(self):
        print (f"Balance:{self.account_balance}")
        return self

    def yield_interest(self):
        self.account_balance=(self.account_balance * self.int_rate) + self.account_balance
        return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()
Scott = BankAccount()
Michael = BankAccount()
Scott.make_deposit(100).make_deposit(100).make_deposit(150).make_withdrawal(75).yield_interest()
print(Scott.account_balance)
Michael.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(50).yield_interest()
print(Michael.account_balance)

BankAccount.all_balances()