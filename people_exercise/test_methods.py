from customer import Customer
from employee import Employee

# create a couple of employees
employee_one = Employee("One", "Employee", 1122)
employee_two = Employee("Two", "Employee", 1123)

customer_one = Customer("One", "Customer", 2131)
customer_two = Customer("Two", "Customer", 2131)

employee_one.set_hourly_rate(4.5)
employee_two.set_hourly_rate(7.5)

employee_one_salary = employee_one.calculate_salary(37.5)
employee_two_salary = employee_two.calculate_salary(20)

customer_one.set_credit_balance(500)
customer_two.set_credit_balance(1500)

customer_one.make_purchase(45)
customer_two.make_purchase(120)

customer_one_balance = customer_one.get_credit_balance()
customer_two_balance = customer_two.get_credit_balance()

employee_one.print_payslip()
employee_two.print_payslip()

customer_one.print_statement()
customer_two.print_statement()
