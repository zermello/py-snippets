from abc import ABC, abstractmethod

class enforce(ABC):
    @abstractmethod
    def engine_start():
        pass

class Bike(enforce):
     def engine_start():
            pass

class Car(enforce):
    def engine_start():
            pass

class truck:
    def engine_start():
            pass

obj1 = Bike()
obj2 = Car()
obj3 = truck()