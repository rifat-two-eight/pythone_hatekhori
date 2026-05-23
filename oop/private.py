class Account:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

acc1 = Account("brac_bank",5000)
print(acc1.name)
print(acc1.__balance)