# pincode variables
pincode = 1234
supplied_pin = None

# failed_attempts variable
failed_attempts = 0

# output message variables
# optional but reduces repetition and risk of typos
please_enter_your_pin_message = "Please enter your pin: "
please_enter_a_number_message = "Whoops! Please enter a number!"
please_enter_4_numbers_message = "Whoops! This needs to be 4 numbers!"
well_done_message = "Nicely done! Have some cash"
locked_out_message = "OOPS! You are locked out!"
incorrect_attempt_message = "Incorrect attempt number: "

# --- WHILE LOOP ---

# this while loop does not include answers which are too long,
# too short or not numeric in the failed_attempts count
# failed_attempts are only added if they are numeric and
# 4 characters

# loop while supplied_pin is not equal to the hardcoded pincode
while supplied_pin != pincode:
    # read pin input from terminal
    supplied_pin = input(please_enter_your_pin_message)

    # check that the input is numeric
    if not supplied_pin.isdecimal():
        print(please_enter_a_number_message)
        continue

    # check that the input is 4 characters
    if not len(supplied_pin) == 4:
        print(please_enter_4_numbers_message)
        continue

    # convert the input from a string into a number
    # this should work without error as we've checked above
    # whether it is a number or not so this code should
    # only be hit if the supplied_pin is numeric
    supplied_pin = int(supplied_pin)

    # if the supplied pin does not match increment the failed attempts variable by 1
    if supplied_pin != pincode:
        failed_attempts += 1

        # nested - if the failed attempts variable is now 3 print "Locked out" and exit loop
#       # else if failed attempts is still < 3 run the loop again and print the number of failed attempts
        if failed_attempts == 3:
            print(locked_out_message)
            break
        else:
            print(incorrect_attempt_message, failed_attempts)

    # if the pin entered matches the pin hardcoded above then print well done and break the loop
    else:
        print(well_done_message)
        break

# --- FOR LOOP ---

# The for loop only gives the user 3 attempts to get their pin
# wrong.  It will alert them if they have entered a value which
# is too long, too short, or not numeric, but it will count as a
# failed attempt

# give the user a limited number of times to try and input their PIN correctly
for i in range(1, 4):

    # read in the user input
    supplied_pin = input(please_enter_your_pin_message)

    # check that the input is numeric
    if not supplied_pin.isdecimal():
        print(please_enter_a_number_message)
        continue

    # check that the input is 4 characters
    if not len(supplied_pin) == 4:
        print(please_enter_4_numbers_message)
        continue

    # convert the input from a string into a number
    # this should work without error as we've checked above
    # whether it is a number or not so this code should
    # only be hit if the supplied_pin is numeric
    supplied_pin = int(supplied_pin)

    # if this is the third attempt display they are locked out, end
    # if the pin matches display well done and break
    # else display wrong number
    if i == 3:
        print(locked_out_message)
    elif supplied_pin == pincode:
        print(well_done_message)
        break
    else:
        print(incorrect_attempt_message, i)
