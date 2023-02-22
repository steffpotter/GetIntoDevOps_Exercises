# create a blueprint (a class) for a bank account
class Account:
    number_of_accounts = 0

    # constructor
    def __init__(self, opening_amount):
        self._balance = opening_amount
        Account.number_of_accounts += 1

    # ########### DATA ############

    # getter (reads the value of the data stored within
    # an instance of an object
    def get_balance(self):
        return self._balance

    # getter
    def get_firstname(self):
        return self._firstname

    # setter
    def set_firstname(self, firstname):
        self._firstname = firstname

    # properties - getter
    @property
    def lastname(self):
        return self._lastname

    # properties - setter
    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    # @ is a decorator
    # a decorator is something which adds functionality

    # ########### FUNCTIONALITY ############

    # deposit method
    def deposit(self, amount):
        self._balance += amount

    # withdraw method
    def withdraw(self, amount):
        # check that the amount is not a negative number
        if amount < 0:
            print("Nice try")
        # check that the user isn't going to take out more
        # money than they actually have
        elif self._balance > amount:
            self._balance -= amount
        else:
            print("Something went wrong")

    # overload __str__
    def __str__(self):
        return "Bank account has a balance of " + str(self._balance)
