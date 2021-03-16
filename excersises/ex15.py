from sys import argv # Imports function argv from module sys

# Declare two variables, script and file name and asign argv to them
script, filename = argv

# Open the file and assign it to txt object
txt = open(filename)


# Print the content of the text file using the function read from object txt
print(f'Here\'s your file {filename}')
print(txt.read())

# Create a new variable file_again input and ask the user to input
# the file name once again
print('Type the filename again:')
file_again = input('> ')

# Open the file again and assign it to the txt_again objecvt
txt_again = open(file_again)

# Print the read of the object txt_again
print(txt_again.read())

# Close the txt object
txt.close()

# Close the txt_again object 
txt_again.close()
