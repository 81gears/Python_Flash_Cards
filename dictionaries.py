# Dictionaries is a set of items
# Each item consists of a key and a value.
# You define a dictionary using braces.

phones ={'i-phones': 'i-5', 'Samsung': 's-7', 'LG':'V-5' }

# have to type exactly the key

# You access the Value associated with the key by stating the dictionary name, Followed by[ ]
phones['i-phones']
# result  'i-5'

# Add items to an existing Dictionary by placing the new key in brackets and providing the value:
phones['Nokia'] = 'g-flip'

# Remove items from a dictionary using the del keyword:
# del phones['i-phones']
# This removes both the key and the value

____________________________________________

# The get() method returns the value associated
# with a key if that key exists in the dictionary.
# if the key does not exist, get() returns None, not an error

# phones.get('i-phones')

# the methods keys(), values(), and items() return different aspects of a dictionary
# that also help you to loop through the dictionary

phones.keys()
phones.values()
phones.items()

#_________________

# Looping through a dictionary to access just the keys.

for phone in phones:
    print(f"Phone:{phone}")

# Looping through a dictionary to access just the values.

for phone in phones.values():
    print(f"Phone:{phone}")

# To Work with both keys and values, use the items()

for phone in phones.items():
    print(f"Phone:{phone},{model}")

# One use of a Dictionary is to represent a collection of key-value paris with
# a consistent structure, such as a glossary.

python_terms = {
    'loop': 'repeated action',
    'list': 'ordered collection',
    'dictionary': 'keys and values',
    }

# another use of dictionary is for every key represents a term.
# and every value represents a meaning.
# or we can use information about one kind of object to a topic.

c_berry = {
    'first': 'Tim',
    'last' : 'Jackson',
    'age': '35',
    }

# How to store a Dictionary in a List.
# It can be helpful to store a collection of Dictionaries in a list.

musicians=[]
phones ={'i-phones': 'i-5', 'Samsung': 's-7', 'LG':'V-5' }
boats={'sea worthy':'Island Packet','racing':'hobbie 18','curising':'tartan',}

for musician in musicians:
    boat=f"{musician['sea worthy']}"
    print(boat)

#_________________________________

# a Dictionary key can be associated with a list of values:

states_visited = {
    'eric':['Texas','Arizona','Florida']
    'amy':['New York', 'Ohio', 'Main'],
    }

for name, states in states_visited.items():
    print(f"{name}has visited:")
    for state in states:
        print(f" {state}")
        

    
    

    














