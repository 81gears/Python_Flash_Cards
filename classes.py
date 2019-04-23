# Classes are at the heart of object-oriented programming.
# Classes allow you to store information and actions to perform on that information
# in one place. Understanding classes will allow you to write code that models
# just about anything in the real world.

# a class organizes code that combines data and actions. To use a class,
# You make an instance of the class. An attribute is a variable associated with
# a class, and a method is a function associated with a class.

# This class represents a trail, such as a hiking trail, with two attributes,
# self.dest and self.len, and one method,  __init__():

class Trail():
    """ A class to represent trails."""

    def __init__(self, dest, len=0):
        self.dest = dest
        self.len = len

# Python classes generally use initial capital letters.
# when an instance of a class is made, the __init__(): methos runs automatically.
# In this code, __init__() requires one argument, dest, and has one optional
# parameter, len.

# The first parameter, self, references the current instance of the class.
# Attaching the values dest and len to self makes them avaiable to all methods
# in the class and any instance of the class.

#___________________________________

# After defining a class, you can add methods that allow you to take actions
# using the class.

# This method generates a description of a trail and prints that description:

class Trail():
    """ A class to represent trails."""

    def __init__(self, dest, len=0):
        self.dest = dest
        self.len = len

    def describe_trail(self):
        """ Print a description os trail. """
        desc= f"This trail goes to {self.dest}."
        if self.len:
            desc += f"\nThe trail is {self.len}km."
        print(desc)

# Each method is automatically sent a reference of the instance of the class,
# so each method needs a self parameter. Then the method can use any attribute
# from the class. In this code, the description includes the trail;s destination
# and its length if it's specified.

