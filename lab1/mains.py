from Cat import Cat
from Dog import Dog
from Snake import Snake
 #
def main():
    #using polymorphism to get sounds from different animals
    animals = [Cat(), Dog(), Snake()]
    for animal in animals:
        animal.talk()
        animal.sound()


main()
