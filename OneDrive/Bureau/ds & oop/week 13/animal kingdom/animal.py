from abc import ABCMeta, abstractmethod


class Animal(object, metaclass = ABCMeta):
    def __init__(self, legs = 0, fins = 0, wings = 0):
        self.legs = legs
        self.fins = fins
        self.wings = wings

    @abstractmethod
    def move(self):
        pass
 
    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def reproduce(self) -> str:
        return f'Members of thins kingdom reproduce by finding a mate of the same species'
    
    def __repr__(self) -> str:
        return f'Kingdom: Animalia'
    

    



