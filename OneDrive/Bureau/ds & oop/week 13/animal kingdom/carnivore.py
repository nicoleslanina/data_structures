from heterotroph import Heterotroph

class Carnivore(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print('I eat meat')

    def __repr__(self) -> str:
        result = '\nThis organism is a carnivore, it feeds on other animals, and its physical features facilitate hunting.'
        return super().__repr__() + result