'''import os

input_file = open("C:\Malini\Precision\codepractice\data.txt","r")
#Assign the object "input_file" read function
#to a variable
var_text = input_file.read()

#print the data in one go
print(var_text)
#Close the File stream handler
input_file.close()'''
'''
import os

# ReOpen the file
input_file1 = open("C:\Malini\Precision\codepractice\data.txt","r")

# While true enter into an infinite loop (we handle it by a break)
while True:
    curr_line = input_file1.readline() # Read line by line, to variable current line
    if not curr_line:
        break                          # Break if there is no line to read
    print(curr_line)                   # Print the current line

# Close the File stream handler
input_file1.close()
'''

import os
readlines_file = open("C:\Malini\Precision\codepractice\data.txt","r")

# Prints the file contents as a LIST
print(readlines_file.readlines())

readlines_file.close()

