from lib.pet import Pet
# import ipdb


class Dog(Pet): 
    def __init__(self, name, age, breed, temperament, sound, loyalty, color):
        super().__init__(name, age, breed, temperament)
        self.sound = sound
        self.loyalty = loyalty
        self.color = color
        
    def talk(self):
        print("Woof woof")
        
    def print_pet_details(self):
        super().print_pet_details()
        print(f'''              sound: {self.sound}
            loyalty: {self.loyalty}
            color: {self.color}
            ''')
        
# ipdb.set_trace()