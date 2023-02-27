from person import Person
from insufficientFundsException import InsufficientFundsException


# define subclass called Customer which inherits from Person
class Customer(Person):

    # constructor
    def __init__(self, firstname, lastname, account_number):
        super().__init__(firstname, lastname)
        self._credit_balance = None
        self._account_number = account_number

    # set the credit balance for the customer
    def set_credit_balance(self, credit_balance):
        self._credit_balance = credit_balance

    # find out the balance
    def get_credit_balance(self):
        return self._credit_balance

    # deduct a purchase from the credit balance
    def make_purchase(self, purchase_amount):
        if purchase_amount > self._credit_balance:
            raise InsufficientFundsException("You don't have enough to do that")
        else:
            self._credit_balance -= purchase_amount

    # throw an exception if the purchase is greater than the credit balance

    # overload the str method for this object
    # calls the __str__ method from the base class
    def __str__(self):
        return f"Customer Number: {self._account_number}" + super().__str__()
