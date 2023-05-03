#!/usr/bin/env python3
# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 
import ipdb
class Pet:
    count = 0 
# 3. ✅ Demonstrate __init__ 
    # Add arguments to instances  
    # use dot notation to access their attributes 
    # update attributes with new values 
    # properties of pets: 
    # name
    # species
    # age
    # size
    # temperment
    def __init__(self, name, species, age, size, temperment):
        self.name = name
        self.species = species
        self.size = size
        self.age = age
        self.temperment = temperment
        Pet.count += 1  
        # instance variable: variable that belongs to the each instance of the class
        # class variable: variable that belongs to the class
        
# 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes
#     Review the self keyword 
#     Invoke the print_pet_details on an instance 
#           -> 
            # name:rose
            # age:11
            # breed:domestic longhair
            # temperament:sweet
            # image_url:rose.jpg
    def print_pet_details(self):
        print(f'''
              name: {self.name}
              age: {self.age}
              temperament: {self.temperment}
              size: {self.size}
              species: {self.species}
              ''')
    def get_details_in_one_line(self):
        print(f"{self.name} is a {self.species}, who is {self.temperment} and {self.size} in size and {self.age} years old.")
        
    @classmethod
    def get_pet_count(Pet): 
        print(f"There are {Pet.count} pets")
# Demonstrate instances 
    # Different Instances are Different Objects
# Demonstrate __init__
# Demonstrate instance method
# Demonstrate the self keyword 
# Stretch Goals
# Demonstrate object properties

# Instances 

# Run in ipdb session
# rose == cookie
#   False

#Read Attributes 
# rose.name -> rose
# rose.age -> 11

#Update
# rose.age -> 11
# rose.age = 12
# rose.age -> 12

spot = Pet("Spot", "Dog", 6, "medium", "Playful")
rose = Pet("Rose", "Cat", 4, "small", "Crazy")

ipdb.set_trace()