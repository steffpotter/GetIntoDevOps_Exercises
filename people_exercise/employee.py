from person import Person
from workedTooMuchException import WorkedTooMuchException

# define subclass called Employee which inherits from Person
class Employee(Person):

    # constructor
    def __init__(self, firstname, lastname, employee_number, hourly_rate):
        super().__init__(firstname, lastname)
        self._hourly_rate = hourly_rate
        self._employee_number = employee_number

    # find out the balance
    def get_hourly_rate(self):
        return self._hourly_rate

    # method to calculate salary
    def calculate_salary(self, hours_done):
        if hours_done > 37.5:
            raise WorkedTooMuchException(hours_done)
        else:
            return self._hourly_rate * hours_done

    # throw an exception if the number of hours is greater than 37.5
    # as that should be the most that anyone should work in one week

    # overload the str method for this object
    # calls the __str__ method from the base class
    def __str__(self):
        return f"Employee Number: {self._employee_number}" + super().__str__()
