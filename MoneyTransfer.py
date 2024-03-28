class MoneyTransfer:
    @staticmethod
    def transfer(sender_account, receiver_account, amount):
        if 0 < amount <= sender_account.balance:
            sender_account.withdraw(amount)
            receiver_account.deposit(amount)
            print(f"Transfer of ${amount} from {sender_account.name} to {receiver_account.name} successful.")
        else:
            print("Invalid transfer amount or insufficient funds.")