from animal import Animal

class Amphibian(Animal):
    def reproduce(self) -> str:
        result = '\nAmphibians reproduce by laying soft eggs in the water.'

        return super().reproduce() + result
    
    def __repr__(self) -> str:
        return super().__repr__() + '\nClass: Amphibian'
    
    