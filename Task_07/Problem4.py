class ShoppingCart:
    def __init__(self):
        self.items = []
        self.quantities = []

    def addItem(self, item, quantity):
        self.items.append(item)
        self.quantities.append(quantity)

    def removeItem(self, item):
        if item in self.items:
            index = self.items.index(item)
            self.items.pop(index)
            self.quantities.pop(index)
        else:
            print("Item Not Found!")

    def calculateTotal(self):
        return sum(self.quantities)
    
    def display(self):
        print("Current Items in Cart:")
        for i in range(len(self.items)):
            print(f"{self.items[i]} - {self.quantities[i]}")
        print(f"Total Quantity: {self.calculateTotal()}")

# Create and test the cart
cart = ShoppingCart()
cart.addItem("Papaya", 100)
cart.addItem("Guava", 200)
cart.addItem("Orange", 150)

# Display initial cart
cart.display()

# Remove item and show updated cart
cart.removeItem("Orange")
print("\nUpdated Items in Cart after removing Orange:")
for i in range(len(cart.items)):
    print(f"{cart.items[i]} - {cart.quantities[i]}")
print(f"Total Quantity: {cart.calculateTotal()}")

        
