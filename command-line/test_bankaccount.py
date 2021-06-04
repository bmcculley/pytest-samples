import pytest
from bank_account import BankAccount

class TestBankAccount():
	test_account = BankAccount()

	def test_deposit(self):
		assert self.test_account.deposit(100) == "Amount deposited: 100.00"

	def test_withdraw(self):
		assert self.test_account.withdraw(50) == "You withdrew: 50.00"

	def test_overdraw(self):
		assert self.test_account.withdraw(51) == "Insufficient balance."

	def test_display(self):
		assert self.test_account.display() == "Net Available Balance: 50.00"
