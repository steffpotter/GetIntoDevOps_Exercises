#!/usr/bin/python

# Example Python script

# import the sys module to give access to command line arguments
# comma delimited list of modules
# (same as using in c#)
import sys

# find out how many arguments have been passed in
# and assign it to our own variable
# argv - argument vector (vector = list)
argc = len(sys.argv)

# if there is more than 1 argument passed in
# print "Too many args"
# otherwise print "Hello World"
if argc > 1:
    print("Too many args")
else:
    where = "World"
    print("Hello", where)

# print "Goodbye from " <first argument in sys.argv array>
print("Goodbye from " + sys.argv[0])
