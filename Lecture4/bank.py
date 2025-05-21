class bankAccont:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            print(f"Old balance: {self.__balance}")
            self.__balance += amount
            print(f"Deposited: {amount}")
            print(f"New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            print(f"Old balance: {self.__balance}")
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"New balance: {self.__balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance")
    
    def get_balance(self):
        print(f"Name: {self.owner}")
        print(f"Balance: {self.__balance}")
        return None

Nicolas = bankAccont("Nicolas", 1000)
Dylan = bankAccont("Dylan", 2000)
Nicolas.deposit(500)
Nicolas.withdraw(200)
Nicolas.get_balance()



