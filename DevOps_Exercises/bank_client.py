from account import Account
from savings_account import SavingsAccount

# create an object instance from the class (called instantiation)
lisa_account = Account(300)
bart_account = Account(4)


def print_balances():
    global lisa_balance, bart_balance
    # get the balance on each account and store it in a variable
    lisa_balance = lisa_account.get_balance()
    bart_balance = bart_account.get_balance()
    # print the balances
    print(f"Lisa has ${lisa_balance} and Bart has ${bart_balance}")


# call print balance method
print_balances()

# deposit money into the account
lisa_account.deposit(50)

# call print balance method
print_balances()

# withdraw money from the account
lisa_account.withdraw(100)
lisa_account.withdraw(-100)
lisa_account.withdraw(300)

# call print balance method
print_balances()

if hasattr(lisa_account, "__str__"):
    print("Lisa has an __str__")
    print(lisa_account)
    print(type(lisa_account))

# OUTPUT
# Lisa has an __str__
# <account.Account object at 0x0000025EB8351F10>
# <class 'account.Account'>

print(lisa_account)
print(bart_account)

# using getters and setters
lisa_account.set_firstname("Lisa")
print(lisa_account.get_firstname())

# using properties
lisa_account.lastname = "Simpson"
print(lisa_account.lastname)

# create savings accounts
lisa_savings_account = SavingsAccount(1000, 0.1)
marge_savings_account = SavingsAccount(200, 2.3)

# set personal info on Marge's account
# using setter
marge_savings_account.set_firstname("Marge")
# using property
marge_savings_account.lastname = "Simpson"

# print the interest rate
print(marge_savings_account.get_interest_rate())

# set the interest rate to something different
marge_savings_account.set_interest_rate(4)

# print the interest rate again to prove it has changed
print(marge_savings_account.get_interest_rate())
