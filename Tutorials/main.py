from Car import *
from EmptyCar import *
from Airplane import *


# instantiate some objects
vehicle = Vehicle()
empty = EmptyCar()
plane = Airplane()
car = Car(4, 4, 100, make="Toyota")
car2 = Car(4, 2, make='Hyundai')

print("#######################")
print(f'The basic Vehicle: --> {vehicle}')
print(f'The empty car: --> {empty}')
print(f'The first car: --> {car}')  # it was the fourth vehicle created
print(f'The second car: --> {car2}')  # it was the fifth vehicle created
print("#######################\n")

print("#######################")
empty.set_speed(25.0)  # we haven't defined set_speed or get_speed for EmptyCar, but they still work - inheritance!
print(f"The empty car's speed: --> {empty.get_speed()}")
print(f"The empty car's repr: --> {repr(empty)}")
print("#######################\n")

print("#######################")
car.set_colour('red')
print(f"The first car's repr: --> {repr(car)}")
print(f"The airplane's repr: --> {repr(plane)}")
print("#######################\n")

print("#######################")
print(f'Is the car moving? --> {Vehicle.is_moving(car)}')
print("Setting the speed of the car to 100.")
car.set_speed(100)  # this won't work because we didn't start the engine
print(f'Is the car moving? --> {car.is_moving()}')
print(f"The car's speed: --> {car.get_speed()}")  # 0.0 because the engine isn't started
print("Let's start the engine...")
car.start_engine()
#vehicle.start_engine()  # the vehicle has no such method; inheritance only goes one way
#car.set_speed(100)
print(f'Is the car moving? --> {car.is_moving()}')
print("#######################\n")

print("#######################")
print("POLYMORPHISM")
print()

def driving(some_vehicle):
    """
    A function for demonstrating polymorphism.
    :param some_vehicle: an object of the Vehicle class or one of its subclasses.
    :return: None
    """
    print(f"This function was passed: --> {repr(some_vehicle)}")
    some_vehicle.set_speed(200)
    print(some_vehicle.get_speed())


def start_it(some_vehicle):
    """
    A function for demonstrating that polymorphism has limitations.
    :param some_vehicle: a Car object
    :return: None
    """
    print(f"This function was passed: --> {repr(some_vehicle)}")
    some_vehicle.start_engine()

new_vehicle = Vehicle()
new_car = Car()
print("The first call:")
driving(new_vehicle)
print()
print("The second call:")
driving(new_car)
print()
print("BE CAREFUL!")
print("Let's call the start_it function:")
start_it(new_car)
#start_it(new_vehicle)
print("#######################\n")

#help(Vehicle)
#help(str)
#help(int)
#help(dict())




