from Vehicle import *


class Airplane(Vehicle):
    """
    A class that defines an Airplane object. Used to demonstrate a simple constructor.
    """
    def __init__(self, capacity=0, speed=0.0):
        super().__init__(speed, colour='grey')  # override the superclass's init to change default colour
        self._capacity = capacity

