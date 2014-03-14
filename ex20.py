# Importing the argv into the code
from sys import argv

#Definiting that the argv includes the script, and the input file
script, input_file = argv

# Defines a methof that prints the result of reading whatever f is
# inputted in as
def print_all(f):
    print f.read()

# Seek apperantly sets the current position of the file. This sets it
# back to 0
def rewind(f):
    f.seek(0)

# A function that takes a count and a file and prints the line number
# and then reads one line. Once it is done reading, it resets that
# 'head' - which is why you don't need to tell it to move to the next
# line. The number incrementing is only used for display.
def print_a_line(line_count, f):
    print line_count, f.readline()

#Opens the input file
current_file = open(input_file)


print "First, let's print the whole file:\n"

#Prints the current file - calling open and then read
print_all(current_file)

print "Now let's rewind, kind of like a tape."

#Sets the file back to 0
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
