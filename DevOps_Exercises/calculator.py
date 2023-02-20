# add
def add(number1, number2):
    return number1 + number2


# add an undefined quantity of numbers together
# variadic function
def add_lots(*numbers):
    return sum(numbers)


# the first parameter is a variadic parameter which will be unpacked,
# any subsequent parameters need to be passed as a named variable
def add_lots_with_message(*numbers, message):
    result = sum(numbers)
    return message + " " + str(result)


# subtract
def subtract(number1, number2):
    return number1 - number2


# multiply
def multiply(number1, number2):
    return number1 * number2


# multiply
def multiply_force_var_name(*, number1, number2):
    return number1 * number2


# divide
def divide(number1, number2):
    return number1 / number2


# divide with a default value for number2
def divide_with_default(number1, number2=5):
    return number1 / number2


# anything after the * in the function declaration needs
# to be passed in by name when calling the function
# anything before the * doesn't need to be passed with the
# name.  Named variables can be passed in any order because
# they are explicitly assigned.
def print_stuff(name, *, age, colour, food):
    print(f"Your name is {name}")
    print(f"Your age is {age} years old")
    print(f"Your favourite colour is {colour}")
    print(f"Your favourite food is {food}")


# **params in a function declaration means the function is
# expecting a dictionary
# ** rarely used **
def print_stuff_keywords(**info):
    print(f"Your name is {info.name}")
    print(f"Your age is {info.age} years old")
    print(f"Your favourite colour is {info.colour}")
    print(f"Your favourite food is {info.food}")


# lambda functions - anonymous functions
# they cannot contain branches or loops
# they *can* contain conditional expressions
# they cannot have return statements or assignments
# often used with map()
compare = lambda a, b: -1 if a < b else (+1 if a > b else 0)


print("a>b", compare(42, 3))
