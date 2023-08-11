import numpy as np
import matplotlib.pyplot as plt

from physical_object import Object_with_mass, tuple_3

class Simple_3d_plotter:
    def __init__(self):
        self.fig = plt.figure()
        self.ax  = self.fig.add_subplot(111, projection='3d')
        plt.ion()
        self.min_plot_limits = tuple_3(0,0,0)
        self.max_plot_limits = tuple_3(10, 10, 10)
        self.points = []
        

    def _setupAxis(self, name):
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title(name)
    
    def _resize_plot(self):
            self.ax.set_xlim(self.min_plot_limits.x, self.max_plot_limits.x)
            self.ax.set_ylim(self.min_plot_limits.y, self.max_plot_limits.y)
            self.ax.set_zlim(self.min_plot_limits.z, self.max_plot_limits.z)

    def _sizePlotToFit(self, location: tuple_3):
        #increase max
        if self.max_plot_limits.x < location.x:
            self.max_plot_limits.x = location.x * 2
        if self.max_plot_limits.y < location.y:
            self.max_plot_limits.y = location.y * 2
        if self.max_plot_limits.z < location.z:
            self.max_plot_limits.z = location.z * 2

        #decrease min
        if self.min_plot_limits.x > location.x:
            self.min_plot_limits.x = location.x * 2
        if self.min_plot_limits.y > location.y:
            self.min_plot_limits.y = location.y * 2
        if self.min_plot_limits.z > location.z:
            self.min_plot_limits.z = location.z * 2
        

    def draw(self, objects : [], time: str):
        self.ax.clear()  # Remove previous plot
        self._setupAxis("Universe dT: " + time)

        for obj in objects:
            self._sizePlotToFit(obj.position)
            self.ax.scatter(obj.position.x, obj.position.y, obj.position.z, color=obj.color, marker='o', s=25)
            # Draw their trail
            self._resize_plot()

        plt.pause(0.1)

