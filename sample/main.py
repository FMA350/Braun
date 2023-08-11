# Python libs
import numpy as np
import signal
# Braun files
from cli_controls import print_welcome
from Universe import Universe
from signalhandlers import PrintHandler, ExitHandler
from simple_plotter_3d import Simple_3d_plotter


def simple_simulation(u : Universe):
    print ("Creating 3 objects")
    u.createRandomObject("Venus", 'y')
    u.createRandomObject("Mars", 'r')
    #u.createRandomObject("Earth", 'b')
    plotter = Simple_3d_plotter()
    simulation_running = True
    step = 0
    while(simulation_running):
        u.simple_universe_tick()
        plotter.draw(u.objects, str(step))
        step += 1
        

def main():
    print_welcome()
    u = Universe() 
    signal.signal(signal.SIGINT,  ExitHandler(u))
    signal.signal(signal.SIGTSTP, PrintHandler(u))
    simple_simulation(u)

if __name__ == '__main__':
     main()