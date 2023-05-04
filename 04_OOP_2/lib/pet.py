#!/usr/bin/env python3
# Class Attributes and Methods 

# import ipdb;
class Pet:
    
    count = 0

    def __init__(self,name, age, breed, temperament):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        Pet.count += 1
 
    
    # 6✅. Create a class method that will print the pet count
    @classmethod
    def pet_count(cls): 
        print(f"The number of pets: {cls.count}")

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}''')
        
# ipdb.set_trace()




