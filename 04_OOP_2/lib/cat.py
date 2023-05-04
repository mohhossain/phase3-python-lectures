#6✅. Create a subclass of Pet called Cat

from lib.pet import Pet
    # Update the instance in debug.py to rose = Cat('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)

# super class: the parent class : pet
# subclass: any class that inherits from a parent class : cat
class Cat(Pet):
    
    def __init__(self, name, age, breed, temperament, sound, loyalty):
        
#8✅. Create __init__ that takes all the parameters from Pet and a parameter called indoor 
    # Use super to pass the Pet parameters to the super class
    # Add an indoor attribute
        super().__init__(name, age, breed, temperament)
        
        self.sound = sound
        self.loyalty = loyalty
#7✅. Create a method unique to the Cat subclass called talk which returns the string "Meowwwwwww"

    def talk(self):
        print("Meeeeeoooooooooowwwwwww")

# polymorphism: use the same function defition but does something same/unique to the class
# there are 2 ways to achieve polymorphism

# overriding : keeping the same name and number of arguments but the body of the function is entirely different 
# overloading : same name but different number of arguments ❌

#9✅. Stretch: Create a method called print_pet_details, to match the print_pet_details in Pet    
        #Add super().print_pet_details() and print the indoor attribute
        
    def print_pet_details(self):
        super().print_pet_details()
        print(f'''          sound: {self.sound}
            loyalty: {self.loyalty}
            ''')
        # return 1 + 1
        
        
        
