from physical_object import Object_with_mass, GenerateRandomObject

# 1) Must be able to swap different simulation methods out.
# 2) Acts as a container for all objects in the universe
# 3) Must support single thread, multithread, and GPU computation.


class Universe:
    def __init__(self) -> None:
        self.objects = []
        self.time_delta = 1.0

    def speedup(self):
         self.time_delta *= 2
        
    def slowdown(self):
         self.time_delta /= 2

    def createRandomObject(self, name: str) -> None:
        obj = GenerateRandomObject(name)
        obj.Display()
        self.addObject(obj)
    
    def addObject(self, object) -> None:
         self.objects.append(object)

    def simple_universe_tick(self) -> None:
        for object in self.objects:
            object.CalculateAcceleration(self.objects)  
        for object in self.objects:
            object.CalculateDeltaSpeed(self.time_delta)
            object.CalculateDeltaPosition(self.time_delta)

    def printAllObjects(self) -> None:
        print("")
        print("*********************************************")
        for obj in self.objects:
                obj.Display()
        print("*********************************************")
        print("")
