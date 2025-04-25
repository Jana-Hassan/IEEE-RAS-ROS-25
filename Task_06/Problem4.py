class Stack:
    def __init__(self):
        self.s = [10, 20, 30, 40, 50]

    def push(self, Num):
        self.s.append(Num)

    def pop(self):
        self.s.pop()


    def display(self):
        print(f"Stack items: {self.s}")


stack = Stack()

stack.display()

print(f"Popped item: {stack.pop()}")  
print(f"Popped item: {stack.pop()}")  
stack.display() 


    