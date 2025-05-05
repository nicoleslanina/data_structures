from heterotroph import Heterotroph

class Herbivore(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print('I eat plants.')

    def __repr__(self) -> str:
        result = '\nThis organism is herbivore. It feeds on plant matter and its physiology facilitates food search'
        return super().__repr__() + result
    