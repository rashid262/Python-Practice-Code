class InventoryItem:
    def __init__(self, item_name, price, quantity):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Item Name: {self.item_name}, Price: {self.price}, Quantity Available: {self.quantity}")

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Updating quantity to {self.quantity}...")
        print(f"New Quantity Available: {self.quantity}")

    def update_amount(self, new_amount):
        self.price = new_amount
        print(f"Updating price to {self.price}...")
        print(f"New Price: {self.price}")


item = input()
price = float(input())
quantity = int(input())

inveit1 = InventoryItem(item, price, quantity)
inveit1.display_info()
new_price = float(input())
new_quantity = int(input())

inveit1.update_amount(new_price)
inveit1.update_quantity(new_quantity)