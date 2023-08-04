# Python libs
import numpy as np
import signal
# Braun files
from cli_controls import print_welcome
from Universe import Universe
from signalhandlers import PrintHandler, ExitHandler
#from VisualEditor import VisualEditor


def simple_simulation(u : Universe):
    print ("Creating 2 objects")
    u.createRandomObject("Venus")
    u.createRandomObject("Mars")
    simulation_running = True
    while(simulation_running):
        u.simple_universe_tick()

def main():
    print_welcome()
    u = Universe() 
    signal.signal(signal.SIGINT,  ExitHandler(u))
    signal.signal(signal.SIGTSTP, PrintHandler(u))
    simple_simulation(u)


if __name__ == '__main__':
     main()