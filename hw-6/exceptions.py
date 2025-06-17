"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __init__(self, message):
        self.message = "Low Fuel: " + message


class NotEnoughFuel(Exception):
    def __init__(self, message):
        self.message = "Not Enough Fuel: " + message


class CargoOverload(Exception):
    def __init__(self, message):
        self.message = "Cargo Over load: " + message
