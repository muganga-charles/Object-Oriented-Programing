from Animal import Animal
class Snake(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Snake"

    def sound(self):
        print(f"Hiss")