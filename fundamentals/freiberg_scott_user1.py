from freiberg_scott_bank_account import BankAccount
class User:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.account = BankAccount({"int_rate" : 0.02, "balance": 0})
        return self

    def make_deposit(self, amount):
        self.account.make_deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.make_withdrawal(amount)
        return self

    def display_user_balance (self, account_balance):
        print(self.display_account_balance())
        return self



    # def transfer_money(self, other_user, amount):
    #     self.account_balance -= amount
    #     other_user.account.make_deposit(amount)
    #     print(f"{self.first_name} transfered {amount} to {other_user.first_name}")
    #     print(f"{self.first_name} new balance == {self.account_balance.balance}")
    #     print (f"{other_user.first_name} new balance = {other_user.account_balance.balance}")

