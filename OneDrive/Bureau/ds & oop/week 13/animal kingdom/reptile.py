from animal import Animal

class Reptile(Animal):
    def reproduce(self) -> str:
        result = '\nReptile reproduce by laying eggs, tipically on land rather than water.'

        return super().reproduce() + result
    
    def __repr__(self) -> str:
        return super().__repr__() + '\nClass: Reptile'
    
    