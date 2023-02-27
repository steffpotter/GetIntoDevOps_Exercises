from customer import Customer
from employee import Employee
from insufficientFundsException import InsufficientFundsException

# method to print a customer statement
def print_statement(customer):
    print(f"\n*** Customer Statement ***")
    print(str(customer))
    print(f"Remaining Credit: {customer.get_credit_balance()}")


# method to print an employee payslip
def print_payslip(employee, hours_worked):
    print(f"\n*** Employee Payslip ***")
    print(str(employee))
    print(f"Hourly rate: {employee.get_hourly_rate()}")

    try:
        print(f"Salary: {employee.calculate_salary(hours_worked)}")
    except Exception as ex:
        print(str(ex))


# create a couple of employees
employee_one = Employee("One", "Employee", 1122, 4.5)
employee_two = Employee("Two", "Employee", 1123, 7.75)

# create a couple of customers
customer_one = Customer("One", "Customer", 2131)
customer_two = Customer("Two", "Customer", 2131)

# give the customers a credit balance
customer_one.set_credit_balance(500)
customer_two.set_credit_balance(1500)

# make a purchase for each customer
try:
    customer_one.make_purchase(1000)
except InsufficientFundsException as ex:
    print(str(ex))
finally:
    print_statement(customer_one)

customer_two.make_purchase(120)

# print employee payslips
print_payslip(employee_one, 37.5)
print_payslip(employee_two, 40)

# print customer statements
print_statement(customer_one)
print_statement(customer_two)

