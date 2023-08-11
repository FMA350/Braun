import numpy as np
from numpy import random
from math import sqrt

from constants import Gconst

class tuple_3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def Display(self) -> None:
        print("x: " + str(self.x) + ", Y: " + str(self.y) + ", Z: " + str(self.z))

class Object_with_mass:
    _max_trail_size = 2

    def __init__(self, name, position: tuple_3, speed: tuple_3, mass, color: str = 'b'):
        self.name     = name
        self.position = position      # Meters from center
        self.speed    = speed         # Meters/Seconds
        self.mass     = mass          # Kilograms
        self.acceleration = tuple_3(0,0,0)
        self.color = color
        self.trail_data = np.array([])
 #previous positions
        np.append(self.trail_data, self.position)


    def _update_trail_data(self):
        self.trail_data = np.append(self.trail_data, tuple_3(self.position.x,self.position.y,self.position.z))
        if(len(self.trail_data) > self._max_trail_size ):
            np.delete(self.trail_data, 0)

    def _calculate_distance(self, other: tuple_3):
        d = pow(2, self.position.x * other.x) + pow(2, self.position.y * other.y) + pow(2, self.position.z * other.z)
        return sqrt(d)

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
                pass
            else:
                #F = G(m1 m2)/r^2
                #A = F/m
                d = self._calculate_distance(object.position)
                a = abs(Gconst * object.mass / pow(2.0, d))
                # a^2 = pow(x2 - x1) + pow(y2 - y1) + pow(z2 - z1)
                ax = a * abs((self.position.x - object.position.x)) / d
                if self.position.x > object.position.x:
                    ax = ax * -1
                ay = a * abs((self.position.y - object.position.y)) /d
                if self.position.y > object.position.y:
                    ay = ay * -1
                az = a * abs((self.position.z - object.position.z)) / d
                if self.position.z > object.position.z:
                    az = az * -1

                self.acceleration.x = ax
                self.acceleration.y = ay
                self.acceleration.z = az
        
    def CalculateDeltaSpeed(self, time_delta):
        # Speed = a*T
        self.speed.x = self.speed.x + (self.acceleration.x * time_delta)
        self.speed.y = self.speed.y + (self.acceleration.y * time_delta)
        self.speed.z = self.speed.z + (self.acceleration.z * time_delta)

    def CalculateDeltaPosition(self, time_delta):
        # FinalP = InitialP + S * T
        self.position.x = self.position.x + (self.speed.x * time_delta)
        self.position.y = self.position.y + (self.speed.y * time_delta)
        self.position.z = self.position.z + (self.speed.z * time_delta)
        self._update_trail_data()

def GenerateRandomObject(name) -> Object_with_mass:
    position_seed = random.randint(10)
    position = random.rand(3) * position_seed
    speed_seed = random.randint(10)
    speed    = random.rand(3) * speed_seed
    mass_seed = random.randint(10000000, 100000000)
    mass = random.rand(1) * mass_seed
    return Object_with_mass(name, tuple_3(position[0],position[1],position[2]), tuple_3(speed[0],speed[1],speed[2]), mass)
    #return Object_with_mass(name, tuple_3(position[0],position[1],position[2]), tuple_3(0,0,0), mass)

