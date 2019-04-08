# Python3
# Simple Data types.

# Comments begin with the # hash mark.
# Comment is a line of text thats ignored by the Python interpreter.

# ____________________

# a Variable is a lable for a value you want to use in your program.
# Variable names in Python follow two main rules:
# Variables must contain only letters, underscores, and numbers.
# Variables must start with a letter or underscore.
# Variables can hold a small piece of information, or it can hold many GB of info.

first_name = ' Tom '
last_name = ' Henderson '
age = 35

#________________________________________

# a String is a vaule made up of one or more characters,
# surrounded by single or double qoutes.

message = " I love Python ! "
print(message)
# I love Python

# insert tabs and newlines into strings using the special sequences \t and \n:

list1 = " Grocery list:\n\tmilk\n\teggs "
print(list1)

# There is no limit on the lenght of a string.

#_________________________________________________

# String methods is a function that performs an action on a string.

name = ' sTephiane goNzales '
name.title()
# name.upper()
# name.lower()
# name.lstrip()
# name.rstrip()
# name.strip

shadow = ' you cAnt See me when Im WorKing '


# String methods are useful for presenting data in certain formator cleaning up.

#______________________________________________________

# Using Variables in Strings.
# in Python3.6 you can usea variable directly inside a string:

username = ' John '
print(f" Welcome back, {username}! ")

# The f is short for format and tells Python to  insert the value of the variable
# listed in braces inside the string.
# This tellPython to format the string using the given variable's value.

# in Python3.5 and earlier, youmust use the format() method

admin = ' Umar '
msg = " Welcome back, {}!".format(admin)
print(msg)

#_______________________________________________

# Numerical Data
# a Interger, or int,is a number that dosent have a decimal point.
# a Float has a decimal point.

# type()function identifies the data type of its argument.

type(3)
type(5.8)

# the Float() function converts a interger into a float.

float(8)

# the int() function converts a float into a interger.
int(5.5)
# the int() function alsoconverts strings to intergers.
int('5')

#_____________________________________

# Numerical Operations

2+5
3-2
2-7

# the round functionrounds a float to thegiven number of decimal places.

round(3.1415926)

# the abs() function returns the absolute value of a number.
abs(-7)

# the bin(), oct(),and hex() function convert base 10 numbers.
bin(20)
oct(20)
hex(20)

# the complex() function represents complex numbers:

complex(2, 3)

# using Math Library

#_________________________________
