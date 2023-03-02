from Animal import Animal
class Cat(Animal):#m
    def __init__(self):
        super().__init__()
        self.name = "Cat"
    def sound(self):
        print(f"Meow")
