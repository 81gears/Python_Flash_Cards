# a Function is a block of code you give a name to so you can use it again.
# Calling its name runs the entire block of code.

def hello1():
    " Greet everyone. "
    print(" Hello, everyone! ")
hello1()    

# to call the function use the function name with parentheses
# hello()

# a parameter is information the function needs to do its work.
# an Argument is a value passed to a function.

# to define parameters for a function, place then within the parentheses in
# the function definition.


def hello(name):
    " Greet someone by name "
    print(f" Hello, how are you {name}! ")
hello("mike")

#def say_hi(person):
 #   print(" Hi " + person + ", how are you doing?")
#say_hi("Alex")


# when a function needs more than one value, it must match the values it
# receives to its parameters.
# Using positional arguments, the function matches the first value it receives 
# to the first value it receives to the first parameter, and so on.

# this functionaccepts a message and a username and posts a message summary:

def post_msg(msg, user):
    " Post a message from the user."
    print(f'{user}: {msg}')

post_msg(" I love Python3.", " Mike ")
post_msg(" Me too ! ", "Amy")

#_______________________________________________

# an asterisk * before a parameter name allows a  function to receive any number
# of positional arguments.
# use it when you dont know how many arguments the function will receive.

# this function accepts a username and the number of messages the user posts.
# the arguments make a tuple :

def post_msg(user, *msgs):
    " Post all of a user's messages. "
    print(f"{user} said:")
    for msg in msgs:
        print(f" {msg}")

post_msg(" Mike ", " I love mountains. ",
         " I love rivers .",
         " I love the ocean .")

# the first argument must provide a value for the first parameter.
# the rest are placed into the tuple msgs.
# here's the output

# I love mountain
# I love rivers .
# I love the ocean .

# a function can only have one parameter that collects an arbitrary number of
# positional arguments.

# keyword arguments specify the parameter a value will be assigned to so you
# can pass arguments in any order.

# in the function call, include the name of the parameter and the value
# to assign to that parameter:

def post_msg15(user, msg):
    " Post a message from a user ."
    print(f"{user}: {msg}")

post_msg15(user=" Tim ",
           msg=" I love Sailboats! ")

# Python assigns the value "Tim" to the parameter user
# " I love sailboats !" to the parameter msg:

# the order of keyword arguments in a function call dosent matter.

#_____________________________________________________________
           
# placing a double asterisk(**) before a parameter allows a function to accept
# an arbiitrary number of keyword arguments.
# use them when you dont know the kind of information the function will receive.
          
# a parameter with ** collects any remaining name-value pairs from
# the function call and adds them to a dictionary.
           
def desc_user(user, **desc):
    " Describe a user "
    print(f" Description of {user}:")
    for key, value in desc.items():
        print(f" {key}: {value}")

desc_user(' Jimmy ', active=True,
          email='mobile81gears@123.com',
          num_posts = 578)
           

# the first argument must be the user. then any remaining keyword arguments are
# packed into the desc dictionary:           
           
#________________________________________________________

# setting a parameter's default value allows the function call to use the default
# value unless another value is specified with the call

# this function serves a cup of coffee.
# you can specify the cup size, but if you dont, you will get a 12 oz cup:

def coffee(size=12):
    " Serve a cup of coffee. "
    print(f"Here's your {size} oz coffee!")

coffee()
coffee(16)

# default value are helpful because they make some arguments optional.
#_____________________________________________________

# return values
# a function sends a return value back to the line that called the function.
# the value can be used later in the code.
# the calling line uses a variable to store the return value.

# this function accepts a rectangle's width and height and returns the area:

def area_rect(w, h):
    " Calculate the area of a rectangle. "
    area = w * h
    return area

my_area = area_rect(5, 4)
print(my_area)

# when the function is called, the return value is stored in the variable my_area.

# you can return any kind of value. to return more than one value, place
# the values in parenthese to return them as a tuple.



    


 

