import calculator

x = 5
y = 10

add_result = calculator.add(y, x)
add_lots_result = calculator.add_lots(y, x, y, x, y, x, y, x)
add_lots_with_message_result = calculator.add_lots_with_message(y, x, y, x, y, x, y, x, message="The answer is:")
multiply_result = calculator.multiply(y, x)
multiply_force_var_name_result = calculator.multiply_force_var_name(number1=y, number2=x)
divide_result = calculator.divide(y, x)
divide_with_default_result = calculator.divide_with_default(y)
subtract_result = calculator.subtract(y, x)

print("Add", add_result)
print("Add lots", add_lots_result)
print("Add lots with message", add_lots_result)
print("Multiply", multiply_result)
print("Multiply (using forced variable names)", multiply_force_var_name_result)
print("Divide", divide_result)
print("Divide with default", divide_with_default_result)
print("Subtract", subtract_result)

calculator.print_stuff("Steff", age=38, colour="Yellow", food="Chocolate")
calculator.print_stuff("Heather", age=10, colour="Pink", food="Sweeties")
calculator.print_stuff("Charlotte", age=10, colour="Orange", food="Mac & Cheese")
