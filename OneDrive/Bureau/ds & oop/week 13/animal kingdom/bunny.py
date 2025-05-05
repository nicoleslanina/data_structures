from pet import Pet
from mammal import Mammal
from herbivore import Herbivore

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        super().__init__(self, legs)
        self.ears = ears


    def __repr__(self) -> str:
        result = '\nSpecies: Bunny'
        result = Mammal.__repr__(self) + result #kingdom, class, species info
        result += '\n' + Pet.__repr__(self) #pet
        return result + '\n' + Herbivore.__repr__(self)
    
    def reproduce(self) -> str:
        result = 'Bunnies can produce multiple litters per year, potentially having 3-8 kits per litter.'

        print(super().reproduce() + '\n' + result)

    def move(self) -> str:
        print('I move by hopping and I can see behind me...')

    def sleep(self) -> str:
        print('Bunnies as nocturnal animals, typically sleep around 12 to 14 hours a day in short intermittent periods.')

    def eat(self) -> str:
        Herbivore.eat(self)
        print('I mostly eat fresh hay and grass with some leafy green and a few pellets. I should only be given fruit and root vegetables, like carrots, as an occasional treat.')
        

if __name__ == '__main__':
    b1 = Bunny()
    print(b1.legs)
    print(b1.ears)

    print()
    b1.reproduce()

    print()
    b1.sleep()

    print()
    b1.move()

    print()
    b1.eat()

    print()
    print(b1.pet())

  



