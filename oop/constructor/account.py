class Account():
    def __init__(self,balance,pin):
        self.balance = balance
        self.pin = pin

    # debit method
    def debit(self,amount):
        self.balance -= amount
        print("taka",amount,"was debitted")
        print("total balance:",self.get_balance())

    # credit method
    def credit(self,amount):
        self.balance+= amount
        print("taka",amount,"was creditted")
        print("total balance:",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(28000,123456)
acc1.debit(500)
acc1.credit(5500)
