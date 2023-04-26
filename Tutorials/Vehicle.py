class Vehicle:

    _vehicle_identification = 100000000  # class attribute

    # CONSTRUCTOR
    def __init__(self, speed=0.0, colour=""):
        """
        A constructor for building Vehicle objects.
        :param speed: the speed of the vehicle, a float
        :param colour: the colour of the vehicle, a string
        """
        self._speed = speed
        self._colour = colour
        self._set_id()  # increment class attribute so different for next instantiation

    # ACCESSORS
    def get_id(self):
        """
        An accessor method for the vehicle's identification number.
        :return:
        """
        return self._id

    def get_speed(self):
        """
        An accessor method for getting the speed of a Vehicle object.
        :return: the Vehicle object's speed, a float
        """
        return self._speed

    def get_colour(self):
        """
        An accessor method for getting the colour of a Vehicle object.
        :return: the Vehicle object's colour, a string
        """
        return self._colour

    # MUTATORS
    def set_speed(self, speed):
        """
        Sets the speed of a Vehicle object. When set, it determines if the Vehicle
        should be in motion or not.
        :param speed: the new speed of the vehicle, a float
        :return: None
        """
        self._speed = speed
        self.is_moving()  # if the speed changes, we run the moving check

    def set_colour(self, colour):
        """
        Sets the Vehicle object's colour.
        :param colour: the new colour, a string
        :return: None
        """
        self._colour = colour

    def _set_id(self):
        """
        Sets the identification number for the Vehicle object.
        :return: None
        """
        self._id = Vehicle._vehicle_identification
        Vehicle._vehicle_identification += 1

    # OTHER METHODS
    def is_moving(self):
        """
        Determines whether the Vehicle object is in motion.
        :return: True if speed is greater than 0.0
                 False otherwise
        """
        if self._speed > 0.0:
            return True
        else:
            return False

    # SPECIAL METHODS
    # overrides default print method
    def __str__(self):
        """
        Returns the vehicle's identification number.
        :return: a string representing vehicle
        """
        return f"The vehicle's identification number is {self._id}."

    # overrides default repr; can be used for rebuilding the instance
    def __repr__(self):
        """
        Returns a string that allows us to rebuild the Vehicle object.
        :return: a string representing the object
        """
        return f'Vehicle({self._speed}, "{self._colour}")'

    # overrides default equality check
    def __eq__(self, other):
        """
        Determines if two Vehicle objects are equal by checking if they have the same speed.
        :param other: the Vehicle object being compared
        :return: True if speed is equal
                 False otherwise
        """
        return self._speed == other.get_speed()

    # overloads the + operator, telling the interpreter what to do with addition
    def __add__(self, other):
        """
        Allows for adding the speed of two Vehicle objects or for adding a float to the speed of the
        Vehicle object.
        :param other: another Vehilce object, float or integer to be added to the Vehicle object
        :return: the new speed, a float
        """
        if isinstance(other, Vehicle):
            return self._speed + other.get_speed()
        return self._speed + other
