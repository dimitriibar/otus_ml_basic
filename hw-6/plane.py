"""
Создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0
    
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
    
    def load_cargo(self, amount):
        if self.cargo + amount <= self.max_cargo:
            self.cargo += amount
        else:
            raise CargoOverload(f"Cannot load {amount} cargo. Current: {self.cargo}, Max: {self.max_cargo}")
    
    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo
