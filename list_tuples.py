# Lists and Tuples
# a List is a collection of items in a specific order.
# [] square brackets indicate a list.

vowels = ['e', 'i', 'o']
vowels[0]
# 'e'
vowels[-1]
# 'o'

# use the append() toadd singleitems to the end of a list.
vowels.append('u')

# use insert() toinsert items at any position using the index of that position:

vowels.insert(0,'a')
vowels

# modify an element in a list using its index.
vowels[-1] ='y'
vowels
# this replaces the last item with y
#_____________________________________________

# removing Items from Lists
# the remove() method removes a specific item from a list.
travel = ['car',' catamran', 'hobbie 18', 'hobbie 16',' flying scott', 'boat', 'train']
travel.remove('boat')
travel

#the del keyword deletes an item at a specific position in the list using its index.
del travel[0]
travel
 # the pop() method removes and returns the last item in a list.
boats = ['catamran', 'hobbie 18', 'hobbie 16',' flying scott'] 
boat = boats.pop()
boat = boats.pop(1)

#___________________________________

#  Slicing a list
# a slice is part of a list that begins with the item at the first index
# specified and stops with the item before thelast index specified:

states = ['ca', 'co', 'ct', 'mn', 'az', 'fl', 'tx', 'wy']
# states[0:5]

# states[:2]
# states[3:]

#_____________________________________________

# Copying a List
# copying a list lets youwork with contents of the copied list without affecting
# the orginal list.

my_states = states [:]

# changes you make to the new list dont affect the orginal list
# my_states.append('co')

#__________________________________

# Looping through lists
# a for loop lets youwork each item in a list,one at a time.

for state in states:
    print(f" I'm flying to{state}.")
    
# loop through part of the list
for state in states[:3]:
    print(f" I've been to{state}.")

# sorting List
# the sorted() function returns a copy of a list in a natural sorted order.

sorted(vowels)

# vowels.sort()

sizes = [1,5,7,2,4]
sorted(sizes)

# reverse sorting
sorted(vowels, reverse=True)

# vowels.reverse()

# a list comprehension is a compact way of defining a list in one line:

#__________________________________________________

# Tuples
# a Tuple you can not modify or change.
# a Tuple is an ordered collection of items that cant be modified. It is usually
# indicated by parenthese:  ()

grades = ('1st', '2nd', '3rd', '4th', '5th')

for grade in grades:
    print(f" Welcome to grade {grade}! ")

