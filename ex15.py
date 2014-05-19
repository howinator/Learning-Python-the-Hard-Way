# This line imports the module for importation of arguments.
from sys import argv

# This line actually grabs the arguments from the command line.
script, filename = argv

# This line opens 'filename'.
txt = open(filename)

# This line just prints the filename to the command line.
print "Here's your file %r:" % filename
# This just reads the file and prints it to the command line.
# Note: *.read() can take a size argument (*.read(size)) to only read some
# number of bytes.
print txt.read()

# This is just prompting the user for the filename again.
print "Type the filename again:"
file_again = raw_input("> ")

# This makes a second instance of the file object for reading.
txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()
