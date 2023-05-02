# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.
# Creating Lists
import ipdb
#1. ✅ Create a list of 10 pet names
# index starts at 0 in python
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Rose', 'Spot', 'Tom', 'Mini', 'Rose', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name 
# print(pet_names[0])


#3. ✅ Return all pet names beginning from the 3rd index
# print(pet_names[3:])

#4. ✅ Return all pet names before the 3rd index
# print(pet_names[:3])

#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
# print(pet_names[3:7])

#6. ✅ Find the index of a given element
# print(pet_names.index('Lea'))

#7. ✅ Reverse the original list
# print(pet_names.reverse())
# pet_names.reverse()
# print(pet_names)

# .reverse() does not create a new list, rather it mutates the original list
#8. ✅ Return the frequency of a given element 
# print(pet_names.count('Rose'))


# Updating Lists
#9. ✅ Change the first element to all uppercase 

# javascript
# pet_names[0].toUpperCase()

# python
# print(pet_names[0].upper())


#10. ✅ Append a new name to the list
# pet_names.append("Luna") #javascript .push
# print(pet_names)

#11. ✅ Add a new name at a specific index
pet_names.insert(5, 'Luna')

# ipdb.set_trace()
#12. ✅ Add two lists together 

pet_names = pet_names + ['Luna', 'Milo', 'Pumpkin']

#13. ✅ Remove the final element from the list
pet_names.pop(2)

#14. ✅ Remove element by specific index
# del pet_names[1]

#15. ✅ Remove a specific element 
# pet_names.remove('Meow Meow Beans')


#16. ✅ Remove all pet names from the list
# pet_names.clear()


#Tuple 
# 📚 Review With Students:
    # Immutable, Unchangeable

#17. ✅ Create a Tuple of pet 10 ages 

pet_age = (12, 12, 14, 2, 6, 9, 17, 3, 5, 8)
# tuple is a list that is immutable and defined using () instead of []
#18. ✅ Print the first pet age
pet_age[0]


# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
# pet_age.pop() #AttributeError: 'tuple' object has no attribute 'pop'


#20. ✅ Attempt to change the first element (should error)
# pet_age[0] = 13 #gives me: TypeError: 'tuple' object does not support item assignment
# ipdb.set_trace()

# Tuple Methods
#21. ✅ Return the frequency of a given element
# print(pet_age.count(12))

#22. ✅ Return the index of a given element 
# print(pet_age.index(8))

#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops

some_range = range(10)
print(some_range)

# for loop

# for pet in pet_names:
#     print(pet)

# for num in range(3, 7):
#     print(pet_names[num])

# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
pets = {'Rose', 'Rose', 'Rose', 'Milo', 'Beans'}
pets2 = {'Rose', 'Spot', 'Tom', 'Mini'}


pet_list = pets.difference(pets2)



# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'rose',
                 'age':11,
                 'breed':'domestic long '}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_spot = dict(name='Spot', age=25, breed='boxer')
# ipdb.set_trace()


# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
print(f"{pet_info_rose['name']} is {pet_info_rose['age']} and a {pet_info_rose['breed']}")
print(f"{pet_info_spot['name']} is {pet_info_spot['age']} and a {pet_info_spot['breed']}")

# print(pet_info_rose['location'])

#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error

# print(pet_info_rose.get('location'))

# Updating 
#29. ✅ Update the pets age to 12
# pet_info_rose['age'] = 12
# print(pet_info_rose)

#30. ✅ Update the other pets age to 26


# Deleting
#30. ✅ Delete a pets age using the "del" keyword 
# del pet_info_rose['age']
# print(pet_info_rose)

#31. ✅ Delete the other pets age using ".pop"
# pet_info_spot.pop('age')
# print(pet_info_spot)

#32. ✅ Delete the last item in the pet dictionary using "popitem()"
pet_info_spot.popitem()
print(pet_info_spot)


# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]

#33. ✅ Loop through a range of 10 and print every number within the range


#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# for (let i = 0; i <= 100; i+2){
#     console.log(i)
# }

# for num in range(50,60, 2):
#     print(num)

#35. ✅ Loop through the "pet_info" list and print every dictionary 
for pet in pet_info: 
    print(pet)


#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument

# def print_names(list):
#     for name in list:
#         print(name)
#37. ✅ Create a function that takes a list as an argument. (simple example) 
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 

def print_names(list): 
    counter = 0
    while counter < len(list):
        print(list[counter])
        counter += 1
        # break

# ipdb.set_trace()


#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dict"s, "name" and "age" as parameters 
        # Create am index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'
            
def update_age(list, name, age): 
    index = 0 
    while index < len(list):
        if(list[index]['name'] == name):
            list[index]["age"] = age
            return list[index]
        index += 1
    return "Pet not found"




# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
# (return / loop / condition )
pet_with_upper_case_names = [ pet['name'].upper() for pet in pet_info if pet['age'] > 2 ]

# find like
#40. ✅ Use list comprehension to find a pet named spot
spot = [ pet for pet in pet_names if pet == 'Spot']
ipdb.set_trace()
# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old
pet_with_upper_case_names = [ pet for pet in pet_info if pet['age'] < 3 ]


#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 

