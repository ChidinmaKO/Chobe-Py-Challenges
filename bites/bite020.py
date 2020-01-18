class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager
    def __enter__(self):
        # return self
        # another way is to copy the transaction
        self.copy_transactions = list(self._transactions)
        return self
    
    def __exit__(self, *args):
        if self.balance < 0:
            # self._transactions.pop()
            self._transactions = self.copy_transactions


# tests
import pytest

from account import Account


@pytest.fixture()
def account():
    return Account()


def test_balance(account):
    assert account.balance == 0
    account + 10
    assert account.balance == 10
    account - 5
    assert account.balance == 5


def test_without_contextman_balance_negative(account):
    assert account.balance == 0
    account - 5
    assert account.balance == -5


def test_with_contextman_performs_rollback(account):
    account + 3
    assert account.balance == 3
    # trigger rollback
    with account as acc:
        acc - 5
    assert account.balance == 3
    # adding this ensures all required dunders are used:
    with account as acc:
        acc + 10
        acc - 3
    assert account.balance == 10