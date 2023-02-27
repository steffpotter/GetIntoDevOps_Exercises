from person import Person


# define subclass called Employee which inherits from Person
class Employee(Person):

    # constructor
    def __init__(self, firstname, lastname, employee_number):
        super().__init__(firstname, lastname)
        self._salary = None
        self._hourly_rate = None
        self._employee_number = employee_number

    # method to set the hourly rate
    def set_hourly_rate(self, hourly_rate):
        self._hourly_rate = hourly_rate

    # method to calculate salary
    def calculate_salary(self, hours_done):
        self._salary = self._hourly_rate * hours_done

    # method to print payslip
    def print_payslip(self):
        print(f"*** Payslip for Employee {self._employee_number} ***")
        print(f"Hourly rate: {self._hourly_rate}")
        print(f"Salary: {self._salary}")
