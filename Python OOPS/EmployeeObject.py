# class Vehicle:
#     delaership_name = "Unknown"
#     total_vehicle = 0
#
#     def __init__(self,make,model,price):
#         self.make = make
#         self.model = model
#         self.price = price
#
#     @staticmethod
#     def dealership_policy():
#         print(f"Dealership Policy: All vehicle comes with 2-year warranty.")
#     @classmethod
#     def increment_vehicle(cls):
#         cls.total_vehicle += 1
#         print(f"Updated Vehicle Count: {cls.total_vehicle}")
#
#
# d_name = input()
# Vehicle.delaership_name = d_name
# make = input()
# model = input()
# price = input()
# v1 = Vehicle(make,model,price)
# Vehicle.increment_vehicle()
# print(f"Dealership: {Vehicle.delaership_name}")
# print(f"Total Vehicle: {Vehicle.total_vehicle}")
# print(f"Vehicle Make: {v1.make}, Model: {v1.model}, Price: {v1.price}")
# Vehicle.dealership_policy()

class Product:
    store_name = "Unknown"
    product_count = 0

    def __init__(self, product_name, product_id, price):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price

    @staticmethod
    def store_policy():
        print("All products come with 30-day return policy.")

    @classmethod
    def increment_product_count(cls):
        cls.product_count += 1
        print(f"Updated Product Count: {cls.product_count}")


s_name = input()
store_name = s_name
p_name = input()
p_id = input()
price = input()

prod1 = Product(p_name, p_id, price)
Product.increment_product_count()
print(f"Store: {Product.store_name}")
print(f"Total Products: {Product.product_count}")
print(f"Product Name: {prod1.p_name}, ID: {prod1.p_id}, Price: {prod1.price}")
Product.store_policy()


