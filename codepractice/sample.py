#print('In this garden{0} plants of{fruits}'.format(' they are',fruits=' oranges'))
#var_integer =2
#var_float =8.9
#var_string = "Teerth"
#print(var_integer, var_float, var_string)
#var100, var200 = 100, 200;
#print("var200 : ", var100);
#print("var200 : ", var200);
A = 1
B = 2
C = 5

# Sum, Difference, product, divide, mod, power
# Add, subtract, multiply 
#print(A+B+C) # OUTPUT: 6
#print(A-B)   # OUTPUT: -1
#print(100/4) # OUTPUT: 33.333333333333336
#print(100%4)
#print(3**5)
#A += 5  # A=A+4
#print(A) # OUTPUT: 5  
# sample string using DOUBLE QUOTES
#var_string_1 = "DOUBLE QUOTES STRING:Welcome to python tutorials by tinitiate.com"

# sample string using SINGLE QUOTES
#var_string_2 = 'SINGLE QUOTES STRING: Welcome to python tutorials by tinitiate.com'

# Multi line string using THREE DOUBLE QUOTES
#var_string_3 = """THREE DOUBLE QUOTES MULTI LINE STRING: Welcome to python 
#tutorials by tinitiate.com,This is a multi line string
#as you can see"""

# print the sthe above strings
#print(var_string_1)
#print(var_string_2)
#print(var_string_3)
## >```
## >### Strings as arrays [Using strings as arrays in other languages]
## >```
# Using python strings as STRING ARRAYs
var_test_string = "Python is cool"

# Index starts from 0, 
# This prints the first character of the string 
#print('First character of variable var_test_string: ', var_test_string[0]);

# Index of the last character is -1
#print('Last character of variable var_test_string: ',var_test_string[-1]);

# Print forth character from the end
#print('Fourth character from the end of variable var_test_string: '
 #      ,var_test_string[5]);

## >```

## >### Slicing Strings[ working with string indexes(character positions in the string)]
## >```
var_test_string = "Python is cool"
# Slicing part of the string using [number:]
# prints string from specified index position to end of string
print(var_test_string[6:])

# prints string from specified index position to end of string
print(var_test_string[-4:])

# prints a part of the string between the specified index position
print(var_test_string[4:10])

# OUT oF range indexes
# when specifing indexes that dont exist is a string
# single index usage fails
#var_my_string  = "four"
# print(var_my_string[5]) # this is raise an error
# Slicing will not raise error, rather will not print anything 
#print(var_my_string[5:7]) # Doesnt print anything 
## >```


