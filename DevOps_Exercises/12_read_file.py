
pelican = open("pelican.txt").read()
print(type(pelican))
print(pelican)

pelican_list = open("pelican.txt").readlines()
print(type(pelican_list))
print(len(pelican_list))

#
for line in pelican_list:
    print(line, end="")
