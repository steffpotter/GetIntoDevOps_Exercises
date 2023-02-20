# open the file and read in the contents
pelican = open("pelican.txt").read()

# print the object type returned by the read() method (str)
print(type(pelican))

# print the entire contents of the file
print(pelican)

# open the file and read the contents into a list
pelican_list = open("pelican.txt").readlines()

# print the object type returned by the readlines() method (list)
print(type(pelican_list))

# get the number of objects in the list using the len() function and print the result
print(len(pelican_list))

# iterate through pelican_list and print each line to the console
# using the end parameter to specify that we don't want a new line created at the end of each print statement
for line in pelican_list:
    print(line, end="")
