import pytest
from banking_app.backend.accounts import BankAccount, SavingsAccount


def test_deposit():
    acc = BankAccount(1001, "John Doe", 100)
    acc.deposit(50)
    assert acc.balance == 150


def test_withdraw():
    acc = BankAccount(1001, "John Doe", 200)
    acc.withdraw(50)
    assert acc.balance == 150


def test_withdraw_insufficient_balance():
    acc = BankAccount(1001, "John Doe", 100)
    with pytest.raises(ValueError):
        acc.withdraw(200)


def test_negative_deposit():
    acc = BankAccount(1001, "John Doe", 100)
    with pytest.raises(ValueError):
        acc.deposit(-20)


def test_savings_interest():
    acc = SavingsAccount(2001, "Jane Smith", 1000, interest_rate=0.05)
    acc.apply_interest()
    assert acc.balance == 1050  # 5% interest
