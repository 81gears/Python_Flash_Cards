# a Conditional Statement checkes for a certain true condition before executing its code.

# every conditional statement has a logical test that evaluates a condition to
# determine whethger its True or False. These values are Boolean values.

if van_cost > 10000:
    print(" That is too much !")

# age == 21 Equality
# age != 21 Inequality
# age < 21  Less than
# age <= 21 Less than or Equal to
# age > 21  Greater than
# age >= 21 Greater than or Equal to

# name == 'Adam'  String Equality
# name !== 'Adam' String Inequality

#________________________________________

# an IF Statement consists of a conditional test on one line and a
# statement or block of statement that run if the test returns True:

if plant_height <3:
    print(" Keep it in the greenhouse! ")

if game_active:
    print(" Lets play ")

# an if-else ststement has an if statement that runs if the condition if True
# and an Else clause that runs if the condition is False.

if plant_height <3:
    print(" Keep it in the greenhouse! ")
else:
    print(" Move it outside ")


# an if-elif-else block has an if statement, a series of test conditions if
# the first test fails, and an else block that runs if all tests fail.
# an if-elif block does not require an else: block

if plant_height < 3:
    print(" Keep it in the greenhouse! ")
    
elif plant_height < 15:
    ptint(" Move it outside")
    
else:
    print(" Ready to Harvest ")

#_________

# User input() function pauses a program and waits for the user to enter data:

name = input(" Whats your name ?")
print(f" Hello, {name} !")

# All Data entered is converted to a string.
# Numerical data needs to be converted to the appropriate type
# before you can work with it:

price = input(" How much for the Van ?")
price = float(price)
if price < 10000:
    print(" I'll take it. ")
else:
    print(" Price is way to high! ")

#________________

# a While loop runs as long as a condition is True:

num = 0
while num < 3:
    num +=1


# a list with at least one item evaluates to True. This loop runs forever
# or until the list is empty.

bugs = [ ' bug1 ', ' bug2 ',' bug3 ']
while bugs:
    bug = bugs.pop(0)
    print(f" Fixing {bug}.")
    print(" All bugs are fixed. ")


# The break statement ends a loop when a certain condition occurs:

while True:
    name = input(" What is your name ?")
    if name == 'quit':
        break
    print(f" Hello, {name}! ")

# the continue keyword breaks the loop and returns to the beginning of the loop.

while True:
    age = input(" How old are you ?")
    age = int(age)
    if age < 5:
        print(" You are a Big Baby !")
    elif age > 60:
        print(" Lets go Running 10 miles ") !"
    else:
        print(f"{age} That is an Great age! ")
        continue

    
    
