# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# bass class
class Vehicle:
    pass

# Vehicle -> GroundVehicle 
class GroundVehicle(Vehicle):
    pass

# Vehicle -> Ground Vehicle -> Car
class Car(GroundVehicle):
    pass

# Vehicle -> Ground Vehicle -> Motorcycle
class Motorcycle(GroundVehicle):
    pass

# Vehicle -> FlightVehicle 
class FlightVehicle(Vehicle):
    pass

# Vehicle -> FlightVehicle -> Airplane
class Airplane(FlightVehicle):
    pass

# Vehicle -> FlightVehicle -> Starship
class Starship(FlightVehicle): 
    pass