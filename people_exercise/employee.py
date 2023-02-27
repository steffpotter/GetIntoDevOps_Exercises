from person import Person


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
        return self._hourly_rate * hours_done

    # overload the str method for this object
    # calls the __str__ method from the base class
    def __str__(self):
        return f"Employee Number: {self._employee_number}" + super().__str__()
