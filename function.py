# writing a function

def say_hello():
    print("I am Mike")

# when we create a a function it is not excatable .
# to excute invoke the function we need to, write the name of the fuction in ()

say_hello()

#________________________

def say_hi(person):
    print(" Hi " + person + ", how are you doing?")
say_hi("Alex")

def move(city):
    print(" I am going to Bsides " + city)
move('Orlando')

#_____________________________

def far2cel(fahr):
    celsius = (5 * (fahr-32))/9
    return celsius

print(" Celsius:", round(far2cel(100),2))
print("Kelvin:", round(far2cel(100)+273.5,2))
