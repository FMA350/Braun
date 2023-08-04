from numpy import random

from constants import Gconst

class tuple_3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def Display(self) -> None:
        print("x: " + str(self.x) + ", Y: " + str(self.y) + ", Z: " + str(self.z))

class Object_with_mass:
    def __init__(self, name, position: tuple_3, speed: tuple_3, mass):
        self.name     = name
        self.position = position # Meters from center
        self.speed    = speed         # Meters/Seconds
        self.mass     = mass          # Kilograms
        self.acceleration = tuple_3(0,0,0)

    def Display(self) -> None:
        print("Object: " + self.name + ", Mass: " + str(self.mass) + "KG")
        print("Position: ")
        self.position.Display()
        print("Speed: ")
        self.speed.Display()
        print("Acceleration: ")
        self.acceleration.Display()

    def CalculateAcceleration(self, objects):
        self.acceleration = tuple_3(0,0,0) #zero the acceleration vector
        for object in objects:
            if object.name == self.name:
                continue
            #F = G(m1 m2)/r^2
            quotient = Gconst * self.mass * object.mass
            ax = quotient / pow((self.position.x - object.position.x),2)
            ay = quotient / pow((self.position.y - object.position.y),2)
            az = quotient / pow((self.position.z - object.position.z),2)

            self.acceleration.x += ax
            self.acceleration.y += ay
            self.acceleration.z += az
        
    def CalculateDeltaSpeed(self, time_delta):
        # Speed = a*T
        self.speed.x += self.acceleration.x * time_delta
        self.speed.y += self.acceleration.y * time_delta
        self.speed.z += self.acceleration.z * time_delta

    def CalculateDeltaPosition(self, time_delta):
        # FinalP = InitialP + S * T
        self.position.x += self.speed.x * time_delta
        self.position.y += self.speed.y * time_delta
        self.position.z += self.speed.z * time_delta

def GenerateRandomObject(name) -> Object_with_mass:
    position_seed = random.randint(100000)
    position = random.rand(3) * position_seed
    speed_seed = random.randint(1000)
    speed    = random.rand(3) * speed_seed
    mass_seed = random.randint(10000000)
    mass = random.rand(1) * mass_seed
    return Object_with_mass(name, tuple_3(position[0],position[1],position[2]), tuple_3(speed[0],speed[1],speed[2]), mass)


