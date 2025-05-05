from abc import ABCMeta, abstractmethod

class Heterotroph(object, metaclass = ABCMeta):
    def __init__(self, legs = 0, fins = 0, wings = 0):
        self.legs = legs
        self.fins = fins
        self.wings = wings

    def eat(self)-> str:
        print("I eat other organisms instead of generating my own food.")

    def __repr__(self) -> str:
        return 'This organism is a heterotroph. It is unable to produce its own food, so it eats other organisms.'
