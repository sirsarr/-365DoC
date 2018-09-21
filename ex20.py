#Excercise 20 -- Functions and Files
from sys import argv

#unpacking script name and file name
script, input_file = argv

#functions definition, function names are explicit
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line (line_count,f):
    print(line_count,f.readline())

#Opening the input file
current_file = open(input_file)

print("First, let's print the whole file:\n")

#running the first function
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

#rewinding the file to read it again, from the begining
rewind(current_file)

print("Let's print three lines:")

#Printing three first lines, line per line
current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line = current_line += 1
print_a_line(current_line,current_file)
