# open the file if it exists, if it doesn't create it
# switch "w" truncates the file contents (so clears the file) and then appends
# switch "a" will append to what is already in the file
poem = open("pelican.txt", "w")

# write the first two lines of the poem to the txt file
# the write method takes in a single object
poem.write("A wonderful bird is the pelican\n")
poem.write("His bill holds more than his belican\n")

# add the remaining lines of the poem to a list
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I can see how the helican\n"]

# write the lines of the list to the file
# the writelines method takes in a collection of objects
poem.writelines(lines)

