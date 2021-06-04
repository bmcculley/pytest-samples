# A simple bank account program

class BankAccount(object):

	def __init__(self):
		self.balance = 0

	# a function to deposit money
	def deposit(self, amount):
		self.balance += amount
		return "Amount deposited: %.2f"% amount

	# a function to withdraw money
	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			return "You withdrew: %.2f"% amount
		else:
			return "Insufficient balance."

	# a function to display the account balance
	def display(self):
		return "Net Available Balance: %.2f"% self.balance


if __name__ == "__main__":
	ba = BankAccount()

	print("Welcome to the Bank Account System:")

	contin = True
	while contin:
		print("""
	1. Make a Deposit
	2. Make a Withdraw
	3. Check Balance
	4. Quit""")
		option = int(input("Choose an option: "))

		if option == 1: 
			amount = float(input("Enter amount to be deposited: "))
			rv = ba.deposit(amount)
			print("\n", rv)
		elif option == 2: 
			amount = float(input("Enter amount to be withdrawn: "))
			rv = ba.withdraw(amount)
			print("\n", rv)
		elif option == 3: 
			rv = ba.display()
			print("\n", rv)
		elif option == 4:
			contin = False
			print("Bye.")
		else:
			print("Invalid option.")
