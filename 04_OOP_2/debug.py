#!/usr/bin/env python3
# 📚 Review With Students:
    # Introduction to Object Oriented programming, classes, instances, methods

# Importing the pet class 
from lib.pet import Pet
from lib.cat import Cat
from lib.dog import Dog

# from lib.dog import Dog

# import Cat from lib.cat

# Instances of the pet classes
rose = Pet('rose', 11, 'domestic longhair', 'sweet')
cookie = Pet('cookie', 1, 'Dachshund', 'hyper')

spot = Cat("Spot", 3, "domestic", "not friendly", "meow", "not loyal")
luna = Dog("Luna", 5, "Golden Retriever", "friendly", "loud barks", "Loyal", "Golden")
# princess_grace = Cat('princess grace', 7, 'domestic longhair', 'affectionate', 'gracy.png')



import ipdb; ipdb.set_trace()