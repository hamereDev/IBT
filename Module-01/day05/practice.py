from abc import ABC, abstractmethod


# Abstract base class
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        print(f"{self.make} {self.model}")

    @abstractmethod
    def wheels(self):
        pass


# Car subclass
class Car(Vehicle):
    def wheels(self):
        return 4


# Truck subclass
class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    # Override describe()
    def describe(self):
        print(f"{self.make} {self.model} - Capacity: {self.capacity}")

    def wheels(self):
        return 6


# Create vehicles
vehicles = [
    Car("Toyota", "Corolla"),
    Truck("Volvo", "FH16", "18 tons"),
    Car("Hyundai", "Elantra"),
    Truck("Scania", "R500", "20 tons")
]


# Polymorphism demonstration
for v in vehicles:
    v.describe()
    print(f"Wheels: {v.wheels()}")
    print("-" * 30)