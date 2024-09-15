import sys
class Account:

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into {self.owner}'s account.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print(f"Insufficient balance. Current balance is {self.balance}.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account.")

    def display_balance(self):
        print(f"{self.owner}'s current balance: {self.balance}")


class PaymentSystem:
    @staticmethod
    def transfer(sender: Account, receiver: Account, amount: float):
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
        elif sender.balance < amount:
            print(f"Transfer failed. {sender.owner} has insufficient balance.")
        else:
            sender.withdraw(amount)
            receiver.deposit(amount)
            print(f"Transferred {amount} from {sender.owner} to {receiver.owner}.")


# if __name__ == "__main__":
#     alice_account = Account("Alice", 500)
#     bob_account = Account("Bob", 300)

#     alice_account.display_balance()
#     bob_account.display_balance()

#     alice_account.deposit(200)

#     bob_account.withdraw(50)

#     PaymentSystem.transfer(alice_account, bob_account, 100)

#     alice_account.display_balance()
#     bob_account.display_balance()
