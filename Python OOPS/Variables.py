class Bank:
    bank_name = "ABC"

    def __init__(self,name,age,bal):
        self.name = name
        self.age = age
        self.bal = bal


b1 = Bank("Rashid",23,55000)
# We can directly access class based variable
print(Bank.bank_name)
# we can call class variables using class name or instance
print(b1.bank_name)
print(b1.name)
print(b1.age)
print(b1.bal)


