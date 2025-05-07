from pet import Pet
from bird import Bird
from omnivore import Omnivore

class Parrot(Bird, Omnivore, Pet):
    def __init__(self, legs = 2, wings = 2, colour = 'yellow'):
        super().__init__(self, legs)
        self.wings = wings
        self.colour = colour
        


    def __repr__(self) -> str:
        result = '\nSpecies: Parrot'
        result = Bird.__repr__(self) + result #kingdom, class, species info
        result += '\n' + Pet.__repr__(self) #pet
        return result + '\n' + Omnivore.__repr__(self)
    
    def reproduce(self) -> str:
        result = 'Parrots often take a few days to lay a full clutch of eggs. This can be as many as three to four eggs.'

        print(super().reproduce() + '\n' + result)

    def move(self) -> None:
        print('I can move in various ways. I can fly, walk, climb and even use a unique method called "beakiation" to travers narrow branches.')

    def sleep(self) -> None:
        print('Parrots sleep around 10 to 12 hours each night, often tucked under their wings. They may also take naps during the day.')

    def eat(self) -> None:
        Omnivore.eat(self)
        print('I eat both plant and nimal matter. My natural diet includes a variety of food like seeds, nuts, fruits, vegetables, flowers, buds, and insects.')
        

if __name__ == '__main__':
    p1 = Parrot()
    print(p1.legs)
    print(p1.wings)

    print()
    p1.reproduce()

    print()
    p1.sleep()

    print()
    p1.move()

    print()
    p1.eat()

    print()
    print(p1.pet())


