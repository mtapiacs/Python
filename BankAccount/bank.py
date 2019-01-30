class Account:                                                                          # Account class!
    def __init__(self, owner, balance=0):                                               # Properties for the account get established to themselves
        self.owner = owner
        self.balance = balance

    def __str__(self):                                                                  # Str result
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'         # f string in order to add elements inside the return as string!

    def deposit(self, dep_amt):                                                         # METHOD .deposit() Only takes one argument when called
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amt):                                                         # METHOD .withdraw() Only takes one argument when called
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


account1 = Account('Miguel', 1000)
print(account1)
print(account1.owner)
print(account1.balance)

account1.deposit(50)
print(account1.balance)

account1.withdraw(150)
print(account1.balance)

account1.withdraw(1000)
print(account1)