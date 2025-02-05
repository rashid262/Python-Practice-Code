class BankAccount:
    def __init__(self,name,account_number):
        self.name = name;
        self.account_number = account_number
        self.__balance = 0
        print("Congratulations! Account Created Successfully")
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully")
            print(f"Final Balance: {self.get_balance()}")
        else:
            print("Enter a positive amount")
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance to withdraw")
        else:
            self.__balance -= amount
            print(f"{amount} withdraw successfully")
            print(f"Final Balance: {self.get_balance()}")
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.get_balance()}")
    def get_balance(self):
        return self.__balance


name = input("Enter Name: ")
acc_number = input("Enter Account Number: ")

acc1 = BankAccount(name,acc_number)
acc1.withdraw(500)
acc1.deposit(1000)
acc1.display_info()
acc1.withdraw(200)
acc1.display_info()

