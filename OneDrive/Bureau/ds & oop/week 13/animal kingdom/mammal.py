from animal import Animal

class Mammal(Animal):
    def reproduce(self) -> str:
        result = '\nMammals give birth to live young, and raise them until they can be independant.'

        return super().reproduce() + result
    
    def __repr__(self) -> str:
        return super().__repr__() + '\nClass: Mammal'
    
    