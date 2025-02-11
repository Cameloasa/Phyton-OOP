"""
Använde Generate från BankAccount
"""
from src.bank_account import BankAccount


def test_balance():
    account = BankAccount(1000)
    assert account.balance() == 1000


def test_deposit():
    assert False


def test_withdraw():
    assert False


def test_apply_interest():
    assert False


def test_can_pay():
    assert False
