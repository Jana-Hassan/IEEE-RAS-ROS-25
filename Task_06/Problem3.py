class Calculator:
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2
    
    def Add(self):
        return self.Num1 + self.Num2
    
    def Subtract(self):
        return self.Num1 - self.Num2
    
    def Multiply(self):
        return self.Num1 * self.Num2
    
    def Divide(self):
        if self.Num2 == 0:
            return "Not Allowed"
        
        return self.Num1 / self.Num2


N1 = float(input("Enter First Number: "))
N2 = float(input("Enter Second Number: "))

calculator = Calculator(N1, N2)

print(f"Addition: {calculator.Add()}")
print(f"Subtraction: {calculator.Subtract()}")
print(f"Multiplication: {calculator.Multiply()}")
print(f"Division: {calculator.Divide()}")

