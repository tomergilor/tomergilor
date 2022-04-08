"""

#_______________________________________________________________________________________________________________

# my_list = [i ** 2 for i in range(1, 11)]        # Generates a list of squares of the numbers 1 - 10
#
# f = open("output.txt", "w")
#
# for item in my_list:
#   f.write(str(item) + "\n")
#
# f.close()
#
#___________
#output:
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100

_____________________________________________________________________________________________________________

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

for value in my_list:
    my_file.write(str(value) + "\n")

my_file.close()
______________________________________________________________________________________________________________

my_file = open("output.txt", "r")

print my_file.read()

my_file.close()

______________________________________________________________________________________________________________

# Declare a new variable my_file and store the result of calling open() on the "text.txt" file in "r"ead-only mode.
# On three separate lines, print out the result of calling my_file.readline(). See how it gets the next line each time?
# Don't forget to .close() your file when you're done with it!)

my_file = open("text.txt", "r")

print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()

_______________________________________________________________________________________________________________________


write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print read_file.read()

read_file.close()

_________________________________________________________________________________________________________________________


with open("text.txt", "w") as my_file:
    my_file.write("My Data!")

if not file.closed:
    file.close()

print my_file.closed
_______________________________________________________________________________________________________________________

"""
