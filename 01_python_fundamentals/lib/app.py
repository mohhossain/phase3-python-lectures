#!/usr/bin/env python3

# 📚 Review With Students:
    # Python environment set up
	# Python debugging tools 
	# Python datatypes 

# 🚨 To enable ipdb debugging, first import "ipdb"
import ipdb

# 1. ✅ Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."

    # Note => Feel free to set your own values for "pet_mood" to view various outputs.

pet_mood = "Hungry!"
pet_name = "Spot"
pet_age = 10
has_eaten = True #True/False starts with a capital
# snake_case
# always has to have a value assigned

if pet_mood == "Hungry!":
    print(f"{pet_name} needs to be fed.")
elif pet_mood == "Rowdy!":
    print(f"{pet_name} needs a walk.") 
else :
    print(f"{pet_name} is all good.")

# print(f"The name of the pet is {pet_name}")
# print(type(pet_age))

# Javascript
# let petMood = "Hungry"
# let petName;
# camelCase

# if(petMood === "Hungry"){
#     console.log("Rose needs to be fed")
# } else if(petMood === "Rowdy!") {
#     console.log("Rose needs to walk")
# }

# console.log(`The name of the pet is: ${petName}`)

# print("Hello world")

# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
    # If pet_food is "Hungry!" => "Rose needs to be fed."
    # In all other cases => "Rose is all good."
    
# javascript
# pet_mood === "hungry" ? console.log("Rose needs to be fed.") : console.log("Rose is all good.")

print("Rose needs to be fed") if pet_mood == "Hungry!" else print("Rose is all good.")

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
    # Test invocation of "say_hello" in ipdb using "say_hello()"
    # say_hello() => "Hello, world!"
    
# javascript

# function say_hello(){
#     return "Hello, world!"
# }

# say_hello()

# python
def say_hello():
    hello_world = "Hello, world!"
    # ipdb.set_trace()
    return hello_world
# print(say_hello())

say_hello()

# ipdb.set_trace()
# def just_a_function():
#     pass

# print(type(just_a_function))

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"
    
def pet_greeting(pet_name = "Luna"):
    return f"{pet_name} says hello!" 

# print(pet_greeting("Rose"))

# javascript
print(pet_greeting("Tyson"))
# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
    # Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
    # pet_status("Rose", "Hungry!") => "Rose needs to be fed."
    # pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
    # pet_greeting("Bud", "Relaxed") => "Bud is all good."
    
    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.

def pet_status(pet_name, pet_mood, is_thirsty):
    if pet_mood == "Hungry!" or not is_thirsty:
        return f"{pet_name} needs to be fed and watered."
    elif pet_mood == "Rowdy!":
        return f"{pet_name} needs a walk"
    else:
        return f"{pet_name} is all good"

ipdb.set_trace()

# javascript
# "2" == 2 #true
# "2" === 2 #false

# python
# "2" == 2 #false
# 2 == 2 #true

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

def pet_birthday(age):
    try:
        age +=1
        print(f"The pet is {age} years old")
    except TypeError:
        if(isinstance(age, str)):
            print("The type of the argument is a string")
        else:
            print("Unknown variable type")
    except UnboundLocalError: 
        print("I have no idea what you")
    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

pet_birthday(10)

print("This is after the function invocation")


# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()


