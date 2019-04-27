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

#_____________________________________

# making instances
# to use class attributes and methods, you must make instances, or objects,
# from the class. The class defines a set of values and actions that represents
# any trail. An instance is a specific set of values that represents a
# Specific trail

# Here we make an instance of Trail and call the method describe_trail():

verst = Trail(" Mt. Verstovia ", 4)
print(f" Destination: {verst.dest}")
verst.describe_trail()

# you provide the class name and include any arguments the __init__()
# method requires. You Assign the instance to a variable,
# and then you can access attributes and call methods using dot notation.

# Heres thye output

Destination: Mt.Verstovia
This trail goes to Mt. Verstovia.
The trail is 4km.

#__________________________________________

# Adding Methods
# A class can have many methods as it needs.

# Here's Trail with a second method defined:

class Trail():
    """ A class to represent trails."""

    def run_trail(self):
        """ Simulate running the trail. """
        print(f" Runningto {self.dest}.")

# each method has the self parameter, giving it access to all the attributes
# in the class.

# Here we make an instance representing a specific trail and call the two methods:

verst = Trail(" Mt. Verstovia ", 4)
verst.describe_trail()
verst.run_trail()

# Here's the output

This trail goes to Mt. Verstovia.
The trail is 4km.
Running to Mt. Verstovia.

#___________________________________________

# Multiple Instances
# You can make many instances as you need from a class.

# Here, the same class generates two trails:

verst = Trail(" Mt. Verstovia ", 4)
verst.describe_trail()
verst.run_trail()

ms = Trail(" Middle Sister", 10)
ms.describe_trail()
ms.run_trail()

# Here is the output:

This trail goes to Mt. Verstovia.
The trail is 4km.
Running to Mt. Verstovia.
This trail goes to Middle Sister.
The trail is 10km.
Running to Middle Sister.

# Each instance maintains its own set of attributes.

#________________________________

# Inheritance
# By using inheritance, you can create a new class that inherits the attributes
# and methods of the original class.

# We will create a class to represent a bike trail:
# the parent class is Trail, and the child class is BikeTrail.

# You define a child class like a normal class but include
# the parent class name in parenthese:

class BikeTrail(Trail):
    """ Represent a bike trail"""

    def __init__(self, dest, len=0):
        super().__init__(dest, len)
        self.paved = True
        self.bikes_only = True

# The Child class __init__() method often needs to call the parent class __init__()
# method by using super().
# The super() function references the parent class allows you to call methods 
# from the parent class:

# The child class can define additional attributes particular to itself.
# for example the self.bikes_only attribute indicates whether
# the trail is closed to nonbicyclists.

#_____________________________________________

# Child Class Methods

# a child class can define its own methods, giving it specific behavior
# the parent class lacks.

# The new BikeTrail method, ride trail(), prints a message thats only appropriate
# for a bike trail:

class BikeTrail(Trail):
    """ Represent a bike trail. """
    def __init__(self, dest, len=0):


    def ride_trail(self):
        """ Simulate riding the trail. """
        print(f" Riding to {self.dest}.")

cross_trail = BikeTrail(" Harbor Mountain ", 5)
cross_trail.ride_trail()

# Heres the output:

Riding to Harbor Mountain.



#_____________________________________

# Overriding Parent Class Methods

# a child class can custmoize the behavior of parent class method by using
# super() to access those methods.

# This BikeTrail class modifies the behavior of the method run_trail():

class BikeTrail(Trail):
    """ Represent a bike trail. """
    def __init__(self, dest, len=0):


    def ride_trail(self):
        """ Simulate riding the trail. """
        if self.bikes_only:
            print(f" Riding to {self.dest}.")
        else:
            super().run_trail()

cross_trail = BikeTrail(" Harbor Mountain ", 5)
cross_trail.ride_trail()

# the method first checks if this is a bikes-only trail: if it is,
# an appropriate message prints:

You cant run this trail!

# if the trail allows runners, the method calls the parent method run_trail(),
# inheriting the behavior of a regular Trail.

#_______________________

# Storing Classes Modules
# You store classes in modules and import them the same way as a functions.

# Here we store the class Trail and BikeTrail in the trails.py file:

class Trail():
    """ A class to represent trails."""

class BikeTrail(Trail):
    """ Represent a bike trail. """

# Now we can import these classes into another file:

from trails import Trail, BikeTrail

verst = Trail(" Mt.Verstovia ", 5)
cross_trail = BikeTrail(" Harbor Mt ", 5)

# Use dot notation to import the entire module:

import trails

verst = Trail(" Mt.Verstovia ", 5)
cross_trail = BikeTrail(" Harbor Mt ", 5)

# Use aliases when importing classes. Store classes to organize your code
# and make the classes available to multiple programs.


