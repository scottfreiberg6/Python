class User:
    def __init__(self,name, email,account_balance):
        self.name=name
        self.email=email
        self.account_balance = account_balance
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
        
    def make_transfer(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
            

michael = User("michael", "m@d.com", 0)
anna = User("anna", "a@d.com", 0)
scott = User("scott", "s@d.com", 0)

scott.make_deposit(100).make_deposit(150).make_deposit(150).make_withdrawal(50)
print(scott.account_balance)

michael.make_deposit(150).make_deposit(150).make_withdrawal(50).make_withdrawal(100)
print(michael.account_balance)

anna.make_deposit(400).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50)
print(anna.account_balance)
