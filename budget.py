class budget2_():
    def __init__(self, balance):
        self.balance = balance

    def __repr__(self):
        return f"The remaining balance is: {self.balance}"

    def withdraw(self, withdrawl):
        self.balance = self.balance - withdrawl
        return  withdrawl
        
    def deposit(self,deposited):
        self.balance = self.balance + deposited
        return deposited