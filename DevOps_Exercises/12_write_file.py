# open the file if it exists, if it doesn't create it
poem = open("pelican.txt", "w")

poem.write("A wonderful bird is the pelican\n")
poem.write("His bill holds more than his belican\n")

lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I can see how the helican\n"]

poem.writelines(lines)

