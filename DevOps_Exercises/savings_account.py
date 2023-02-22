from account import Account


# class definition - inherits from Account
class SavingsAccount(Account):

    # constructor
    def __init__(self, opening_amount, interest_rate):
        super().__init__(opening_amount)
        self._interest_rate = interest_rate

    # getter
    def get_interest_rate(self):
        return self._interest_rate

    # setter
    def set_interest_rate(self, interest_rate):
        self._interest_rate = interest_rate
