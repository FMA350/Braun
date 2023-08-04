# Python libs
import numpy as np
import signal
# Braun files
from object import GenerateRandomObject
#from VisualEditor import VisualEditor


def universe_tick(objects, time_delta):
    for object in objects:
        object.CalculateAcceleration(objects)  
    for object in objects:
        object.CalculateDeltaSpeed(time_delta)
        object.CalculateDeltaPosition(time_delta)
        #object.Display()

objects = []


class ExitHandler:
    def __init__(self, myvar):
        self.myattr = myvar
    def __call__(self, signo, frame):
        exit(myvar)

class PrintHandler:
    def __init__(self):
        pass
    def __call__(self, signo, frame):
        for o in objects:
            o.Display()

def main():
    print ("Creating 2 objects")
    simulation_running = True
    v = GenerateRandomObject("Venus")
    m = GenerateRandomObject("Mars")
    objects.append(v)
    objects.append(m)
    signal.signal(signal.SIGINT,  PrintHandler())
    signal.signal(signal.SIGQUIT, ExitHandler(1))
    while(simulation_running):
        universe_tick(objects, 1)


if __name__ == '__main__':
     main()