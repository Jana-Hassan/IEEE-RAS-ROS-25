class BankAccount:
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    
    def Deposit(self, amount):
        self.balance+= amount

    def Withdrawal(self, amount):
        self.balance-= amount
        
    def bankFees(self, fees):
        self.balance+= 0.05*fees

    def display(self):
        print( f"""
        Account Number :{self.accountNumber}
        Account Name :{self.name}
        Account Balance :{self.balance}
        """)

bankAcoount = BankAccount(217851484, "Ahmed", 2600)
bankAcoount.display()


