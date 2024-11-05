#Write code to demonstrate depositing and withdrawing money while maintaining encapsulation.

class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute to store the balance
        self.__balance = initial_balance

    # Method to deposit and withdraw money to the account
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew: ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    # Getter method to safely access the balance
    def get_balance(self):
        return self.__balance

# Creating an instance of the class
account = BankAccount(1000)  # Account starts with $1000 balance
account.deposit(500)  # Depositing $500
account.deposit(-200)  # Trying to deposit a negative amount (should fail)
account.withdraw(200)  # Withdrawing $200
account.withdraw(2000)  # Trying to withdraw more than the balance (should fail)

# calling the method
print(f"Current balance: ${account.get_balance()}")
