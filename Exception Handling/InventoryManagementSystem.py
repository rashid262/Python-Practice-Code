class Inventory:
    def __init__(self):
        self.products = {}
    def add_product(self,name,quantity):
        if quantity < 0:
            raise ValueError("Addition failed. Quantity must be positive.")
        else:
            if name in self.products:
                self.products[name] += quantity
            else:
                self.products[name] = quantity
        print(f"{quantity} {name} added to inventory. Current quantity: {self.products[name]}")
    def remove_product(self,name,quantity):
        if name not in self.products or quantity < 0 or self.products[name] < quantity:
            raise ValueError(f"Removal failed. Product {name} not found in inventory.")
        else:
            self.products[name] -= quantity
            print(f"{quantity} {name} removed from inventory. Current quantity: {self.products[name]}")

name1, quantity1 = input().split()
name2, quantity2 = input().split()
inv1 = Inventory()
try:
    inv1.add_product(name1,int(quantity1))
except ValueError as e:
    print(e)

try:
    inv1.remove_product(name2,int(quantity2))
except ValueError as e:
    print(e)