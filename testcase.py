# test_bank_account.py
import pytest
from bank_account import BankAccount
from MoneyTransfer import MoneyTransfer


@pytest.fixture
def accounts():
    account1 = BankAccount("Alice", 1000)
    account2 = BankAccount("Bob", 500)
    return account1, account2


def test_deposit(accounts):
    account1, _ = accounts
    initial_balance = account1.balance
    amount = 500
    account1.deposit(amount)
    assert account1.balance == initial_balance + amount


def test_withdraw(accounts):
    _, account2 = accounts
    initial_balance = account2.balance
    amount = 200
    account2.withdraw(amount)
    assert account2.balance == initial_balance - amount


def test_transfer(accounts):
    account1, account2 = accounts
    initial_balance_sender = account1.balance
    initial_balance_receiver = account2.balance
    amount = 300
    MoneyTransfer.transfer(account1, account2, amount)
    assert account1.balance == initial_balance_sender - amount
    assert account2.balance == initial_balance_receiver + amount


def test_invalid_deposit():
    account = BankAccount("Charlie")
    initial_balance = account.balance
    amount = -100
    account.deposit(amount)
    assert account.balance == initial_balance  # Balance should remain unchanged for invalid deposit


def test_invalid_withdraw():
    account = BankAccount("David", 200)
    initial_balance = account.balance
    amount = 300
    account.withdraw(amount)
    assert account.balance == initial_balance  # Balance should remain unchanged for invalid withdrawal


def test_insufficient_funds_transfer(accounts):
    account1, account2 = accounts
    initial_balance_sender = account1.balance
    initial_balance_receiver = account2.balance
    amount = 1500  # More than account1's balance
    MoneyTransfer.transfer(account1, account2, amount)
    assert account1.balance == initial_balance_sender  # Sender's balance should remain unchanged
    assert account2.balance == initial_balance_receiver  # Receiver's balance should remain unchanged



