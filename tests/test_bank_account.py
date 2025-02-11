"""
Använde Generate från BankAccount
"""
import pytest

from src.bank_account import BankAccount


def test_show_balance():
    account = BankAccount(1000)
    assert account.show_balance() == 1000


def test_deposit_amount_negative():
    account = BankAccount(0)
    amount = -20
    with pytest.raises(ValueError, match= 'Beloppet måste vara positiv.'):
        account.deposit(amount)

def test_deposit_amount_positiv():
    account = BankAccount(500)
    account.deposit(100)
    assert account.show_balance() == 600


def test_withdraw_amount_negative():
    account = BankAccount(100)
    amount = - 20
    with pytest.raises(ValueError, match= 'Beloppet måste vara positivt.'):
        account.withdraw(amount)

def test_withdraw_amount_bigger_than_balance():
    account = BankAccount(100)
    amount = 150
    with pytest.raises(ValueError, match= 'Otillräckliga medel.'):
        account.withdraw(amount)


def test_withdraw_amount():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.show_balance() == 50


def test_can_pay():
    account = BankAccount(500)
    assert account.can_pay(300) is True
    assert account.can_pay(600) is False

def test_apply_interest():
    account = BankAccount(1000)
    account.apply_interest(0.05)  # 5% räntan
    assert account.show_balance() == 1050  # 1000 + 5% = 1050

def test_apply_interest_negative():
    account = BankAccount(1000)
    interest = -0.05
    with pytest.raises(ValueError, match= 'Räntan måste vara positiv.'):
        account.apply_interest(interest)