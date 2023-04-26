from Vehicle import *


class Car(Vehicle):

    # CONSTRUCTOR
    def __init__(self, tires=4, doors=4, speed=0.0, colour="", make=""):
        super().__init__(speed, colour)  # call the superclass's init to create inherited attributes (including id)
        self._tires = tires  # new instance attributes
        self._doors = doors
        self._make = make
        self._engine = False

    # NEW ACCESSORS/GETTERS
    def get_tires(self):
        return self._tires

    def get_doors(self):
        return self._doors

    def get_make(self):
        return self._make

    # NEW MUTATORS/SETTERS
    def set_tires(self, number_of_tires):
        self._tires = number_of_tires

    def set_doors(self, number_doors):
        self._doors = number_doors

    def set_make(self, make):
        self._make = make

    # OVERRIDDEN MUTATOR
    def set_speed(self, speed):
        if self.is_engine_running():
            self._speed = speed
        else:
            print("The engine isn't on.")

    # NEW METHODS
    def is_engine_running(self):
        """
        An accessor method to determine if the engine is running.
        :return: True if the engine is running
                False otherwise
        """
        return self._engine

    def start_engine(self):
        if self.is_engine_running():
            print("The engine is already running.")
        else:
            self._engine = True

    def stop_engine(self):
        if not self.is_engine_running():
            print("The engine is already stopped.")
        else:
            self._engine = False

    # OVERRIDDEN METHOD
    def is_moving(self):
        if self.is_engine_running() and self._speed > 0.0:
            return True
        else:
            return False

    # SPECIAL METHODS - OVERRIDDEN
    def __repr__(self):
        return f'Car({self._tires}, {self._doors}, {self._speed}, "{self._colour}", "{self._make}")'
