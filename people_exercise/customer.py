from person import Person


# define subclass called Customer which inherits from Person
class Customer(Person):

    # constructor
    def __init__(self, firstname, lastname, account_number):
        super().__init__(firstname, lastname)
        self._credit_balance = None
        self._employee_number = account_number

    # set the credit balance for the customer
    def set_credit_balance(self, credit_balance):
        self._credit_balance = credit_balance

    # deduct a purchase from the credit balance
    def make_purchase(self, purchase_amount):
        self._credit_balance -= purchase_amount

    # find out the balance
    def get_credit_balance(self):
        return self._credit_balance

    def print_statement(self):
        print(f"*** Invoice for Customer {self._account_number} ***")
        print(f"Remaining Credit: {self._credit_balance}")
